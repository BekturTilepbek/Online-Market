from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import ProductForm, CategoryForm
from webapp.models import Product, Category


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', context={'products': products})


def create_product(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'new_product.html', context={'form':   form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('detail_product', pk=product.pk)
        else:
            return render(request, 'new_product.html', context={'form': form})


def read_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'detail_product.html', context={'product': product})


def create_category(request):
    if request.method == "GET":
        form = CategoryForm()
        return render(request, 'new_category.html', context={'form': form})
    else:
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            return render(request, 'new_category.html', context={'form': form})
