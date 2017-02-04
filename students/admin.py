from django.contrib import admin
from .models import *
# Register your models here.
class students_data_Admin(admin.ModelAdmin):
	list_display=["roll_no","name","created","modified"]
	fields=["roll_no","name","class_name"]
	#readonly_fields = ['password']
admin.site.register(students_data,students_data_Admin)

class students_in_class_dataAdmin(admin.ModelAdmin):
	list_display=["student","class_name"]
admin.site.register(students_in_class_data,students_in_class_dataAdmin)