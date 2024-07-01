from django.urls import path

from webapp.views import index, detail_product

urlpatterns = [
    path('', index, name='products'),
    path('products/', index, name='products'),
    path('products/<int:product_id>/', detail_product, name='detail_product'),
]
