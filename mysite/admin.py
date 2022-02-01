from django.contrib import admin
from mysite.models import OrderItem, Order, ShippingAddress, Customer
from mysite.models import Item
# Register your models here.
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(ShippingAddress)
