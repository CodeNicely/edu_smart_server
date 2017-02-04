from __future__ import unicode_literals

from django.db import models
from classes.models import class_data
from teachers.models import teachers_data
from department.models import department_data
# Create your models here.
class subjects_data(models.Model):
	department=models.ForeignKey(department_data)
	name=models.CharField(max_length=120,blank=False,null=False)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

	def __unicode__(self):
		return str(self.name)

class subjects_class_teacher_data(models.Model):
	subject=models.ForeignKey(subjects_data)
	class_id= models.ForeignKey(class_data)
	teacher= models.ForeignKey(teachers_data)

class subjects_syllabus(models.Model):
	title=models.CharField(max_length=120,blank=False,null=False)
	subject= models.ForeignKey(subjects_data)
	description= models.CharField(max_length=120,blank=False,null=False)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

class subjects_assignments(models.Model):
	title=models.CharField(max_length=120,blank=False,null=False)
	subject= models.ForeignKey(subjects_data)
	file= models.FileField(upload_to='resources/',null=True)
	deadline= models.DateTimeField()
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

class subjects_resources(models.Model):
	subject= models.ForeignKey(subjects_data)
	title=models.CharField(max_length=120,blank=False,null=False)
	file= models.FileField(upload_to='resources/',null=True)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

class subjects_announcements(models.Model):
	subject= models.ForeignKey(subjects_data)
	title=models.CharField(max_length=120,blank=False,null=False)
	file= models.FileField(upload_to='resources/',null=True)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
