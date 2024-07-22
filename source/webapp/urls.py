from django.urls import path

from webapp.views import CategoryListView, CreateCategoryView
from webapp.views import ProductListView, CreateProductView, ProductDetailView, UpdateProductView, DeleteProductView


urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/add/', CreateProductView.as_view(), name='create_product'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/update', UpdateProductView.as_view(), name='update_product'),
    path('products/<int:pk>/delete', DeleteProductView.as_view(), name='delete_product'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/add/', CreateCategoryView.as_view(), name='create_category'),
    path('categories/<slug:slug>/', ProductListView.as_view(), name='category_products')
]
