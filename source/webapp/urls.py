from django.urls import path

from webapp.views import index, read_product, create_product, create_category

urlpatterns = [
    path('', index, name='products'),
    path('products/', index, name='products'),
    path('products/<int:pk>/', read_product, name='detail_product'),
    path('products/add/', create_product, name='new_product'),
    path('categories/add/', create_category, name='new_category')
]
