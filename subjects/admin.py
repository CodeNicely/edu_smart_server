from django.contrib import admin
from .models import *
# Register your models here.
class subjects_data_admin(admin.ModelAdmin):
	list_display=["name","department","created","modified"]
admin.site.register(subjects_data,subjects_data_admin)

class subjects_class_teacher_dataAdmin(admin.ModelAdmin):
	list_display=["subject","class_id","teacher"]
admin.site.register(subjects_class_teacher_data,subjects_class_teacher_dataAdmin)

class subjects_syllabusAdmin(admin.ModelAdmin):
	list_display=["title","subject"]
admin.site.register(subjects_syllabus,subjects_syllabusAdmin)


class subjects_resourcesAdmin(admin.ModelAdmin):
	list_display=["subject","title","file","created"]
admin.site.register(subjects_resources,subjects_resourcesAdmin)

# class subjects_resources(admin.ModelAdmin):
# 	list_display=["title","class_id","teacher","created","modified"]
# admin.site.register(subjects_data,subjects_data_admin)
