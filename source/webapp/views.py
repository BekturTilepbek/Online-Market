from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import Product, Category


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', context={'products': products})


def detail_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'detail_product.html', context={'product': product})


def new_product(request):
    if request.method == "GET":
        return render(request, 'new_product.html', context={'categories': Category.objects.all()})
    else:
        product = Product.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description') if request.POST.get('description') else None,
            category=get_object_or_404(Category, pk=request.POST.get('category')),
            price=request.POST.get('price'),
            image=request.POST.get('image')
        )

        return redirect('detail_product', pk=product.pk)


def new_category(request):
    if request.method == "GET":
        return render(request, 'new_category.html')
    else:
        Category.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description') if request.POST.get('description') else None
        )

        return redirect('products')