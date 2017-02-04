from __future__ import unicode_literals

from django.db import models



class notice_data(models.Model):
	title=models.CharField(max_length=120,blank=False,null=False)
	description=models.CharField(max_length=120,blank=False,null=False)
	author= models.CharField(max_length=120,blank=False,null=False)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

	# def __unicode__(self):
	# 	return str(self.name)

class KEYS_LIST(models.Model):
	key=models.CharField(max_length=120,unique=True)
	def __unicode__(self):
		return str(self.key)

class KEYS(models.Model):
	key=models.ForeignKey(KEYS_LIST,to_field='key')
	value=models.CharField(max_length=120,blank=True,null=True)

class CUSTOM(models.Model):
	key=models.ForeignKey(KEYS_LIST,to_field='key')
	value=models.CharField(max_length=120,blank=True,null=True)