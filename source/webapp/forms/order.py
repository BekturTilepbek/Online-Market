from django import forms
from django.forms import widgets

from webapp.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'phone_number', 'address']
        error_messages = {
            'user': {
                'required': 'Заполните поле'
            },
            'phone_number': {
                'required': 'Заполните поле'
            },
            'address': {
                'required': 'Заполните поле'
            }
        }

        widgets = {
            'user': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'})
        }
