from django.contrib import admin
from django.contrib.admin import AdminSite
from .forms import CustomAuthenticationForm

AdminSite.login_form = CustomAuthenticationForm

