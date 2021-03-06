from django.contrib import admin

from .models import Category, Product



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'date_created')
    list_filter = ['category']
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)