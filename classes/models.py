from __future__ import unicode_literals

from django.db import models
from department.models import department_data
# Create your models here.
class class_data(models.Model):
	name=models.CharField(max_length=120,blank=False,null=False)
	department= models.ForeignKey(department_data,to_field='id')
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
	def __unicode__(self):
		return str(self.department)+' '+str(self.name)

class class_announcements(models.Model):
	class_id= models.ForeignKey(class_data,to_field='id')
	title=models.CharField(max_length=120,blank=False,null=False)
	description=models.CharField(max_length=120,blank=False,null=False)
	file= models.FileField(upload_to='resources/',null=True)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
	author=models.CharField(max_length=120,blank=False,null=False)

class class_assignments(models.Model):
	title=models.CharField(max_length=120,blank=False,null=False)
	description=models.CharField(max_length=120,blank=False,null=False)
	class_id= models.ForeignKey(class_data,to_field='id')
	file= models.FileField(upload_to='resources/',null=True)
	author=models.CharField(max_length=120,blank=False,null=False)
	deadline= models.DateTimeField()
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
