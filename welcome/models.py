from __future__ import unicode_literals

from django.db import models

# Create your models here.
class welcome_data(models.Model):
    image=models.ImageField(upload_to='welcome/',default="/media/welcome/default.png")
    quote=models.CharField(max_length=240,blank=False,null=False)
    modified= models.DateTimeField(auto_now=True,auto_now_add=False)
    created= models.DateTimeField(auto_now=False,auto_now_add=True)
