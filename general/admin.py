from django.contrib import admin
from .models import *
# Register your models here.

class notice_dataAdmin(admin.ModelAdmin):
   list_display=["title","description"]
admin.site.register(notice_data,notice_dataAdmin)

class KEYS_Admin(admin.ModelAdmin):
   list_display=["key","value"]
admin.site.register(KEYS,KEYS_Admin)

class CUSTOM_Admin(admin.ModelAdmin):
   list_display=["key","value"]
admin.site.register(CUSTOM,CUSTOM_Admin)

class KEYS_LIST_Admin(admin.ModelAdmin):
   list_display=["key"]
admin.site.register(KEYS_LIST,KEYS_LIST_Admin)
