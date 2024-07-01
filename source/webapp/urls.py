from django.urls import path

from webapp.views import index, detail_product, new_product, new_category

urlpatterns = [
    path('', index, name='products'),
    path('products/', index, name='products'),
    path('products/<int:pk>/', detail_product, name='detail_product'),
    path('products/add/', new_product, name='new_product'),
    path('categories/add/', new_category, name='new_category')
]
