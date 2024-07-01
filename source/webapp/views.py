from django.shortcuts import render

from webapp.models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', context={'products': products})
