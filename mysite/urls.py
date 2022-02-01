from django.urls import path
from . import views
from mysite.views import (
    ItemDetailView
)
app_name =  'mysite'
urlpatterns = [
    path('', views.index,name='home'),
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('itemDetail/<int:pk>/',ItemDetailView.as_view(),name='item-detail'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('update_item/',views.updateItem,name='update_item'),
    path('process_order/',views.processOrder,name='processOrder'),
]
