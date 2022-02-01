from django import forms
from django.forms import ModelForm
# from ecommerce.mysite.models import UserProfileInfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
# class UserProfileInfoForm(forms.Modelform):
#     class Meta():
#         model = UserProfileInfo

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']