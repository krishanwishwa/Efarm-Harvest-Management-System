from django.contrib import admin
from.models import Workers
from.models import Machines


class EmployeeAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'position', 'gender', 'address', 'email')

admin.site.register(Workers,EmployeeAdmin)
admin.site.register(Machines)
