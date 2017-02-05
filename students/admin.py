from django.contrib import admin
from .models import *
# Register your models here.
class students_data_Admin(admin.ModelAdmin):
	list_display=["id","name","created","modified"]

admin.site.register(students_data,students_data_Admin)

class students_in_class_dataAdmin(admin.ModelAdmin):
	list_display=["student","class_name"]
admin.site.register(students_in_class_data,students_in_class_dataAdmin)