from django.contrib import admin
from .models import *
# Register your models here.
class department_dataAdmin(admin.ModelAdmin):
    list_display=["name","created","modified"]
admin.site.register(department_data,department_dataAdmin)