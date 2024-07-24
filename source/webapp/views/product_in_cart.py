from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View

from webapp.forms import ProductForm, SearchForm, ProductInCartForm
from webapp.models import Product, Category, ProductInCart


class AddProductInCartView(View):

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        if product.remain > 0:
            product_in_cart, created = ProductInCart.objects.get_or_create(product=product, defaults={'quantity': 1})
            print(product_in_cart)
            if not created:
                if product_in_cart.quantity < product.remain:
                    product_in_cart.quantity += 1
                    product_in_cart.save()
                    return redirect('products')
                else:
                    return redirect('products')
            else:
                return redirect('products')


