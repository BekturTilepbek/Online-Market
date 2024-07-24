from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, View

from webapp.models import Product, ProductInCart


class ProductsInCartListView(ListView):
    model = ProductInCart
    template_name = 'product/products_in_cart_list.html'
    context_object_name = 'products_in_cart'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total = 0
        for product_in_cart in ProductInCart.objects.all():
            total += product_in_cart.product.price * product_in_cart.quantity
        context['total'] = total
        return context


class AddProductInCartView(View):

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        if product.remain > 0:
            product_in_cart, created = ProductInCart.objects.get_or_create(product=product, defaults={'quantity': 1})
            if not created:
                if product_in_cart.quantity < product.remain:
                    product_in_cart.quantity += 1
                    product_in_cart.save()
            return redirect(request.META['HTTP_REFERER'])
        return redirect(request.META['HTTP_REFERER'])


class DeleteProductInCartView(View):

    def get(self, request, *args, **kwargs):
        product_in_cart = get_object_or_404(ProductInCart, pk=kwargs.get('pk'))
        if product_in_cart.quantity > 1:
            product_in_cart.quantity -= 1
            product_in_cart.save()
        else:
            product_in_cart.delete()
        return redirect(request.META['HTTP_REFERER'])
