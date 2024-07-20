from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': UserModel.USERNAME_FIELD.capitalize()}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class BaseAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            # field.label = field.label.upper()
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-control form-control-solid'
                
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-check-input'
            


            # if isinstance(field, forms.CharField):
            #     field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-control form-control-solid'
            #     field.label = field.label.capitalize()
            # elif isinstance(field, forms.EmailField):
            #     field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-control form-control-solid'
            # elif isinstance(field, forms.DateField):
            #     field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-control form-control-solid'
            # elif isinstance(field, forms.IntegerField):
            #     field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-control form-control-solid'

            
    class Meta:
        # Define common Meta options if needed
        fields = '__all__'
    