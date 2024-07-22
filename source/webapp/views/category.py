from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import CategoryForm
from webapp.models import Category


def categories_index(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, 'category/categories.html', context={'categories': categories})


def create_category(request):
    if request.method == "GET":
        form = CategoryForm()
        return render(request, 'category/new_category.html', context={'form': form})
    else:
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            return render(request, 'category/new_category.html', context={'form': form})
