from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView
from mysite.models import ShippingAddress
from mysite.models import OrderItem, Order
from django.utils import timezone
from mysite.forms import CreateUserForm
from mysite.models import Item, Customer
import json 
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from . utils import cookieCart, guestOrder
# Create your views here.


def registerPage(request):
    form= CreateUserForm()

    if(request.method =="POST"):
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user)

            return redirect('mysite:login')
        else:
            print( form.errors)
    return render(request,'mysite/register.html',{'form':form})

def loginPage(request):
    if (request.method =='POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('mysite:home')
        else:
            messages.info(request, 'Username OR Password is incorrect')
            return render(request, 'mysite/login.html')
    return render(request,'mysite/login.html')   

def logoutUser(request):
    logout(request)
    return redirect('mysite:login')

def index(request):
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, ordered=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
    products = Item.objects.all()
    context = {'products':products,'cartItems':cartItems}
    return render(request, 'mysite/index.html',context)


class ItemDetailView(DetailView):
    model = Item
    template_name = 'mysite/detail.html'


def cart(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, ordered=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
        print(items)
    return render(request, 'mysite/cart.html',{
        'items':items,
        'order':order,
        'cartItems':cartItems,
    })


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, ordered=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
    return render(request, 'mysite/checkout.html',{
        'items':items,
        'order':order,
        'cartItems':cartItems,
    })

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action: ', action)
    print('productId: ', productId)


    customer = request.user.customer
    item = Item.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, ordered=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, item=item)

    if action== 'add':
        orderItem.quantity +=1
    elif action == 'remove':
        orderItem.quantity -=1
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Item was added", safe=False)

@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, ordered=False)

    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total']) 
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.ordered = True
    order.save()

    ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address1']+data['shipping']['address2'],
        # country=data['shipping']['country']
        state=data['shipping']['state'],
        city=data['shipping']['city'],
        zipcode=data['shipping']['zip'],
        )

    return JsonResponse("Payment Complete", safe=False)