from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    list_filter = ('name', 'price')
    search_fields = ('name', 'price', 'email')

admin.site.register(Product, ProductAdmin)
