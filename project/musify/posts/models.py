# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from persons.models import person
def location(instance,filename):
    return str(instance.author)+'/'+str(filename)

class Post(models.Model):
    author=models.CharField(max_length=120)
    tags=models.CharField(max_length=150)
    title=models.CharField(max_length=120)
    timestamp=models.DateTimeField(auto_now_add=True)
    lyrics=models.CharField(max_length=300,null=True)
    artist=models.CharField(max_length=120)
    content=models.TextField(max_length=6000)
    image=models.ImageField(upload_to=location,blank=True)#Use of imagefield requires you to install pillow

    def __unicode__(self):
        return self.title+','+self.author