from django.urls import path

from webapp.views import (index, create_product, read_product, update_product, delete_product, categories_index,
                          create_category)

urlpatterns = [
    path('', index, name='products'),
    path('products/', index, name='products'),
    path('products/<int:pk>/', read_product, name='detail_product'),
    path('products/add/', create_product, name='new_product'),
    path('products/<int:pk>/update', update_product, name='update_product'),
    path('products/<int:pk>/delete', delete_product, name='delete_product'),
    path('categories/', categories_index, name='categories'),
    path('categories/add/', create_category, name='new_category'),
    path('categories/<slug:slug>/', index, name='category_products')
]
