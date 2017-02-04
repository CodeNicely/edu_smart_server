from django.contrib import admin
from .models import *
# Register your models here.

class class_dataAdmin(admin.ModelAdmin):
    list_display=["name","department","created","modified"]
admin.site.register(class_data,class_dataAdmin)


class class_announcementsAdmin(admin.ModelAdmin):
	list_display=["class_id","title","file","created"]
admin.site.register(class_announcements,class_announcementsAdmin)

class class_assignmentsAdmin(admin.ModelAdmin):
	list_display=["title","class_id","deadline"]
admin.site.register(class_assignments,class_assignmentsAdmin)
