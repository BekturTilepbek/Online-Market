from django.shortcuts import render, get_object_or_404

from webapp.models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', context={'products': products})


def detail_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'detail_product.html', context={'product': product})
