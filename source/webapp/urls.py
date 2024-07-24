from django.urls import path

from webapp.views import CategoryListView, CreateCategoryView
from webapp.views import ProductListView, CreateProductView, ProductDetailView, UpdateProductView, DeleteProductView
from webapp.views import AddProductInCartView, ProductsInCartListView, DeleteProductInCartView


urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/create/', CreateProductView.as_view(), name='create_product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/update', UpdateProductView.as_view(), name='update_product'),
    path('product/<int:pk>/delete', DeleteProductView.as_view(), name='delete_product'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/add/', CreateCategoryView.as_view(), name='create_category'),
    path('categories/<slug:slug>/', ProductListView.as_view(), name='category_products'),
    path('cart/add/product/<int:pk>/', AddProductInCartView.as_view(), name='add_product_in_cart'),
    path('cart/', ProductsInCartListView.as_view(), name='cart'),
    path('cart/delete/product_in_cart/<int:pk>/', DeleteProductInCartView.as_view(), name='delete_product_in_cart'),
]
