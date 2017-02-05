from django.contrib import admin
from .models import *
# Register your models here.
class thread_dataAdmin(admin.ModelAdmin):
	list_display=["title","description"]
admin.site.register(thread_data,thread_dataAdmin)

class message_dataAdmin(admin.ModelAdmin):
	list_display=["author_name","message"]
admin.site.register(message_data,message_dataAdmin)
