from __future__ import unicode_literals

from django.db import models
from classes.models import class_data
import hashlib

# Create your models here.
class students_data(models.Model):
	name=models.CharField(max_length=120,blank=False,null=False)
	password=models.CharField(max_length=1200,blank=False,null=False,default=hashlib.sha512('abcd').hexdigest().lower())
	roll_no=models.CharField(max_length=120,blank=False,null=False)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

	def __unicode__(self):
		return str(roll_no)+' '+str(name)

class students_in_class_data(models.Model):
	student=models.ForeignKey(students_data)
	class_name=models.ForeignKey(class_data)
