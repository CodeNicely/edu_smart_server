from django.contrib import admin
from .models import *
# Register your models here.

class class_dataAdmin(admin.ModelAdmin):
    list_display=["name","department","created","modified"]
admin.site.register(class_data,class_dataAdmin)