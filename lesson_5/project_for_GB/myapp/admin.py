from django.contrib import admin
from .models import User, Product, Orders

class ProductAdmin(admin.ModelAdmin):
    """Список продуктов"""
    list_display = ['name', 'price', 'description']

# Register your models here.
admin.site.register(User)
admin.site.register(Product, ProductAdmin)
admin.site.register(Orders)