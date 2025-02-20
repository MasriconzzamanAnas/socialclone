from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from . import models
from django import forms
from django.contrib.auth.models import User

class signupfrom(UserCreationForm):
    password1= forms.CharField(widget=forms.PasswordInput())
    password2= forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model= User
        fields = ['username','email', 'password1', 'password2']