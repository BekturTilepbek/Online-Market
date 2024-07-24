from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.forms import ProductForm, SearchForm
from webapp.models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = 'product/products_list.html'
    ordering = ['category', 'name']
    context_object_name = 'products'
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        self.slug = kwargs.get('slug')
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        form = self.form
        if form.is_valid():
            return form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(name__icontains=self.search_value) | Q(category__name__icontains=self.search_value)
            )

        if self.slug:
            category = get_object_or_404(Category, slug=self.slug)
            queryset = queryset.filter(category=category)
        queryset = queryset.filter(remain__gt=0)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.form
        if self.search_value:
            context["search"] = urlencode({"search": self.search_value})
            context["search_value"] = self.search_value
        return context


# def index(request, slug=None):
#     if request.GET:
#         products = Product.objects.filter(name=request.GET.get('search'))
#         return render(request, 'product/products_list.html', {'products': products})
#
#     if slug is not None:
#         category = get_object_or_404(Category, slug=slug)
#         products = Product.objects.filter(category=category)
#         products = products.order_by('name')
#         return render(request, 'product/products_list.html', context={'products': products, 'category': category})
#
#     products = Product.objects.order_by('category', 'name')
#     return render(request, 'product/products_list.html', context={'products': products})


class CreateProductView(CreateView):
    template_name = "product/create_product.html"
    form_class = ProductForm

    def get_success_url(self):
        return reverse("product_detail", kwargs={"pk": self.object.pk})


class ProductDetailView(DetailView):
    template_name = "product/product_detail.html"
    model = Product


class UpdateProductView(UpdateView):
    template_name = "product/update_product.html"
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse("product_detail", kwargs={"pk": self.object.pk})


class DeleteProductView(DeleteView):
    template_name = "product/delete_product.html"
    model = Product
    success_url = reverse_lazy("products")
