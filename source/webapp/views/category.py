from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.forms import CategoryForm
from webapp.models import Category


class CategoryListView(ListView):
    model = Category
    template_name = "category/categories_list.html"
    context_object_name = "categories"


class CreateCategoryView(CreateView):
    template_name = "category/create_category.html"
    form_class = CategoryForm

    def get_success_url(self):
        return reverse("category_products", kwargs={"slug": self.object.slug})
