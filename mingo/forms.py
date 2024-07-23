from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm, AdminPasswordChangeForm
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': UserModel.USERNAME_FIELD.capitalize()}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class CustomDateTimeInput(forms.DateTimeInput):
    def __init__(self, attrs=None):
        attrs = attrs or {}
        attrs.update({'class': 'form-control datetimepicker-input'})  # Add your custom CSS class
        super().__init__(attrs=attrs)



class BaseAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            # field.label = field.label.upper()
    
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-select'
            elif isinstance(field.widget, forms.TextInput) or isinstance(field.widget, forms.NumberInput):
                field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-control'
            
            
    class Meta:
        fields = '__all__'

class MingoPasswordChangeForm(AdminPasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm New Password'}))
    

