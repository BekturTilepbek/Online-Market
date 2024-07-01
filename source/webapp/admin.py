from django.contrib import admin

from webapp.models import Category, Product

admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category']
    list_display_links = ['id', 'name']
    list_filter = ['category']
    search_fields = ['name']
    fields = ['name', 'description', 'category', 'price', 'image']


admin.site.register(Product, ProductAdmin)