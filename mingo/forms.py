from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

UserModel = get_user_model()



class CustomAuthenticationForm(AuthenticationForm):
    # Add any customizations to the form here
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': UserModel.USERNAME_FIELD.capitalize()}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


