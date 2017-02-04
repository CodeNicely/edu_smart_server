from __future__ import unicode_literals

from django.db import models
from department.models import department_data
from classes.models import class_data
# Create your models here.
from department.models

class thread_data(models.Model):
	access_level=models.IntegerField()
	department=models.ForeignKey(department_data,to_field='id',null=True)
	class_id=models.ForeignKey(class_data,to_field='id',null=True)

class message_data(models.Model):
	thread_id=models.ForeignKey(thread_data,to_field='id')
	message=models.CharField(max_length=120,blank=False,null=False)
	department=models.ForeignKey(department_data,to_field='id',null=True)
	class_id=models.ForeignKey(class_data,to_field='id',null=True)
	teacher=models.BooleanField(default=False)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
