from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'name', 'employee_id', 'shift', 'arrival', 'remark')   
