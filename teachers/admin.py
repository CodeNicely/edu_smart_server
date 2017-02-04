from django.contrib import admin
from .models import *
# Register your models here.
class teachers_data_Admin(admin.ModelAdmin):
	list_display=["name","department","created","modified"]
	field=["name","department","roll_no"]
admin.site.register(teachers_data,teachers_data_Admin)