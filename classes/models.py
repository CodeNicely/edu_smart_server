from __future__ import unicode_literals

from django.db import models
from department.models import department_data
# Create your models here.
class class_data(models.Model):
	name=models.CharField(max_length=120,blank=False,null=False)
	department= models.ForeignKey(department_data)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
	def __unicode__(self):
		return str(self.department)+' '+str(self.name)