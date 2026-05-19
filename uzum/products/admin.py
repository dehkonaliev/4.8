from django.contrib import admin
from .models import Category, Product, Order

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    search_fields = ['name', 'summary']
    list_filter = ['category']
    

admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Product, AdminProduct)
