from django import forms
from django.forms import widgets

from webapp.models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'image', 'remain']
        error_messages = {
            'name': {
                'required': 'Заполните поле'
            },
            'price': {
                'required': 'Заполните поле',
                'max_digits': 'Вводите до 7 знаков',
            },
            'image': {
                'required': 'Заполните поле'
            },
            'remain': {
                'required': 'Заполните поле',
                'min_value': 'Не вводите числа ниже 0'
            }
        }

        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class': 'form-control', 'cols': 50, 'rows': 5}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'}),
            'remain': widgets.NumberInput(attrs={'class': 'form-control'})
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        error_messages = {
            'name': {
                'required': 'Заполните поле'
            }
        }

        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class': 'form-control', 'cols': 50, 'rows': 5}),
        }