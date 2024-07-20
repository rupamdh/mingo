from django.contrib import admin
from django.contrib.admin import AdminSite
from .forms import CustomAuthenticationForm, BaseAdminForm

AdminSite.login_form = CustomAuthenticationForm

admin.ModelAdmin.form = BaseAdminForm