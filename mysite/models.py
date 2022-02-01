from django.conf import settings
from django.shortcuts import reverse 
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class UserProfileInfo(models.Model):
#     user =models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name or ''
    
class Item(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    listed_date = models.DateTimeField(default=datetime.now(), blank=True)
    image = models.ImageField(upload_to='item_images',blank=True, null=True)
    slug = models.SlugField(default="test-product")
    # quantity = models.IntegerField(default=1)
    def __str__(self):
        return self.title or ''

    def get_absolute_url(self):
        return reverse("mysite:item-detail", kwargs={"pk":self.pk})

    def get_add_to_cart_url(self):
        return reverse("mysite:add-to-cart", kwargs={"pk":self.pk})

    @property   
    def imageURL(self):
        try: 
            url = self.image.url
        except:
            url =''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, blank=True, null=True)
    ordered_date = models.DateTimeField(default=datetime.now(), blank=True)
    ordered = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200)
    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=1)
    order= models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True, null=True)
    date_added = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    @property
    def get_total(self):
        return self.item.price * self.quantity

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True, null=True)
    address= models.CharField(max_length=200, null=True)
    city= models.CharField(max_length=200, null=True)
    state= models.CharField(max_length=200, null=True)
    zipcode= models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.address


    