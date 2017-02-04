from __future__ import unicode_literals

from django.db import models
from classes.models import class_data
from teachers.models import teachers_data
from department.models import department_data
# Create your models here.
class subjects_data(models.Model):
	department=models.ForeignKey(department_data,to_field='id')
	name=models.CharField(max_length=120,blank=False,null=False)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

	def __unicode__(self):
		return str(self.name)

class subjects_class_teacher_data(models.Model):
	subject=models.ForeignKey(subjects_data,to_field='id')
	class_id= models.ForeignKey(class_data,to_field='id')
	teacher= models.ForeignKey(teachers_data,to_field='id')

class subjects_syllabus(models.Model):
	title=models.CharField(max_length=120,blank=False,null=False)
	subject= models.ForeignKey(subjects_data)
	description= models.CharField(max_length=120,blank=False,null=False)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)


class subjects_resources(models.Model):
	subject= models.ForeignKey(subjects_data,to_field='id')
	title=models.CharField(max_length=120,blank=False,null=False)
	file= models.FileField(upload_to='resources/',null=True)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
