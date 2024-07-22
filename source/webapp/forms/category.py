from django import forms
from django.forms import widgets

from webapp.models import Category


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
