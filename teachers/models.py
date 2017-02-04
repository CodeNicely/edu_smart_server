from __future__ import unicode_literals

from django.db import models
from department.models import department_data
import hashlib
# Create your models here.
class teachers_data(models.Model):
	roll_no=models.CharField(max_length=120,blank=False,null=False)
	name=models.CharField(max_length=120,blank=False,null=False)
	department= models.ForeignKey(department_data)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
	password=models.CharField(max_length=1200,blank=False,null=False,default=hashlib.sha512('abcd').hexdigest().lower())

	def __unicode__(self):
		return str(self.name)