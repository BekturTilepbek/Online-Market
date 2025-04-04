from django.contrib import admin

from webapp.models import Category, Product, ProductInCart, Order, OrderProduct


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    fields = ['name', 'description']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category']
    list_display_links = ['id', 'name']
    list_filter = ['category']
    search_fields = ['name']
    fields = ['name', 'description', 'category', 'price', 'image']


class ProductInCartAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity']
    list_display_links = ['id', 'product']
    search_fields = ['product']
    fields = ['product', 'quantity']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'phone_number', 'created_at']
    ordering = ['-created_at']
    list_display_links = ['id']
    search_fields = ['user']
    fields = ['user', 'phone_number', 'address']


admin.site.register(Order, OrderAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductInCart, ProductInCartAdmin)
