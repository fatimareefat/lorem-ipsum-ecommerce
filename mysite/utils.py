import json 
from . models import *


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}


    print('Cart: ', cart)
    items = []
    order={'get_cart_total':0, 'get_cart_items':0}
    cartItems = order['get_cart_items']

    for i in cart:
        print("i: ",i)
        # We use try block to prevent items in cart that may have been removed by seller
        try:
            cartItems += cart[i]['quantity']

            product = Item.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])
            print(product)
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            products = {
                'item':{
                    'id':product.id,
                    'title':product.title,
                    'price':product.price,
                    },
                'quantity':cart[i]['quantity'],
                'get_total':total,
            }
            print(products)
            items.append(products)
            print(items)
        except:
            pass
    return {'items':items,'order':order,'cartItems':cartItems}

def guestOrder(request, data):
    print("User is not logged in")

    print('COOKIES:', request.COOKIES)
    firstName = data['form']['firstName']
    lastName = data['form']['lastName']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(
        email=email,
        )

    customer.firstName = firstName
    customer.lastName = lastName
    customer.save()

    order = Order.objects.create(
        customer=customer,
        ordered=False,
    )

    for item in items:
        product = Item.objects.get(id=item['item']['id'])

        orderItem = OrderItem.objects.create(
            item=product,
            order=order,
            quantity=item['quantity'],
        )
    return customer, order