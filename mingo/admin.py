from django.contrib import admin
from django import forms
from django.contrib.admin import AdminSite
from .forms import CustomAuthenticationForm, BaseAdminForm, MingoPasswordChangeForm
from django.contrib.admin import ModelAdmin
from django.urls import NoReverseMatch, Resolver404, resolve, reverse


#Change the default login form
AdminSite.login_form = CustomAuthenticationForm

#Change the default change form for model
ModelAdmin.form = BaseAdminForm


#Add class to related field like foreignkey select field
def change_formfield_for_foreignkey(original_method):
    def wrapper(self, db_field, request, **kwargs):
        kwargs["widget"] = forms.Select(attrs={"class": "form-select"})
        return original_method(self, db_field, request, **kwargs)
    return wrapper
ModelAdmin.formfield_for_foreignkey = change_formfield_for_foreignkey(ModelAdmin.formfield_for_foreignkey)


#Change the default change password form for user
# def replace_password_change_form(original_method):
#     def wrapper(self, request, extra_context=None):
#         from django.contrib.auth.views import PasswordChangeView
#         defaults = {
#             "form_class": MingoPasswordChangeForm,  # Use your custom form class
#             "extra_context": {**self.each_context(request), **(extra_context or {})},  # Additional context for the template
#         }
#         if self.password_change_template is not None:
#             defaults["template_name"] = self.password_change_template
#         request.current_app = self.name
#         return PasswordChangeView.as_view(**defaults)(request)
#     return wrapper

# # Apply the monkey patch to AdminSite.password_change
# AdminSite.password_change = replace_password_change_form(AdminSite.password_change)




