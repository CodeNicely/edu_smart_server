from django.contrib import admin
from .models import *
# Register your models here.


class welcome_dataAdmin(admin.ModelAdmin):
    list_display=["id","image","quote","modified","created"]
admin.site.register(welcome_data,welcome_dataAdmin)