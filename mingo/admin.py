from django.contrib import admin
from django import forms
from django.contrib.admin import AdminSite
from .forms import CustomAuthenticationForm, BaseAdminForm, MingoPasswordChangeForm
from django.contrib.admin import ModelAdmin

#Change the default login form
AdminSite.login_form = CustomAuthenticationForm

# def change_password_change(original_method, user_id):
#     def wrapper(self, request, user_id, form_class=MingoPasswordChangeForm, extra_context=None):
#         extra_context = extra_context or {}
#         extra_context['title'] = 'Change Password'
#         return original_method(self, request, user_id, form_class, extra_context)
#     return wrapper

# AdminSite.password_change = change_password_change(AdminSite.password_change)

#Change the default change form for model
ModelAdmin.form = BaseAdminForm


#Add class to related field like foreignkey select field
def change_formfield_for_foreignkey(original_method):
    def wrapper(self, db_field, request, **kwargs):
        kwargs["widget"] = forms.Select(attrs={"class": "form-select"})
        return original_method(self, db_field, request, **kwargs)
    return wrapper
ModelAdmin.formfield_for_foreignkey = change_formfield_for_foreignkey(ModelAdmin.formfield_for_foreignkey)

