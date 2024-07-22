from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import ProductForm
from webapp.models import Product, Category


def index(request, slug=None):
    if request.GET:
        products = Product.objects.filter(name=request.GET.get('search'))
        return render(request, 'product/index.html', {'products': products})

    if slug is not None:
        category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=category)
        products = products.order_by('name')
        return render(request, 'product/index.html', context={'products': products, 'category': category})

    products = Product.objects.order_by('category', 'name')
    return render(request, 'product/index.html', context={'products': products})


def create_product(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'product/new_product.html', context={'form':   form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('detail_product', pk=product.pk)
        else:
            return render(request, 'product/new_product.html', context={'form': form})


def read_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/detail_product.html', context={'product': product})


def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        form = ProductForm(instance=product)
        return render(request, 'product/update_product.html', context={'form': form})
    else:
        form = ProductForm(data=request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('detail_product', pk=product.pk)
        else:
            return render(request, 'product/update_product.html', context={'form': form})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        return render(request, 'product/delete_product.html', context={'product': product})
    else:
        product.delete()
        return redirect('products')
