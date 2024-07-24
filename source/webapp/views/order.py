from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import OrderForm
from webapp.models import ProductInCart, OrderProduct, Order


class CreateOrderView(CreateView):
    model = Order
    form_class = OrderForm

    def form_valid(self, form):
        order = form.save(commit=False)
        if ProductInCart.objects.all():
            order.save()
            for product_in_cart in ProductInCart.objects.all():
                OrderProduct.objects.create(
                    order=order,
                    product=product_in_cart.product,
                    product_quantity=product_in_cart.quantity)
            ProductInCart.objects.all().delete()
        return redirect('products')

    def get_success_url(self):
        return reverse("products")
