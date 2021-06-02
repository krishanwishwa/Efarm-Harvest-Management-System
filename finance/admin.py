from django.contrib import admin
from.models import Sales
from.models import Expenses

class SalesAdmin(admin.ModelAdmin):
  list_display = ('id', 'customer', 'product', 'quantity', 'payment', 'payment_method', 'date')

admin.site.register(Sales,SalesAdmin)
admin.site.register(Expenses)
