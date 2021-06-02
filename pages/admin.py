from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
  list_display = ('id', 'product', 'user', 'price', 'email', 'date')

admin.site.register(Product,ProductAdmin)
