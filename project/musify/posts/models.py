# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from persons.models import person
from django.urls import reverse
from django.contrib.auth.models import User



def location(instance,filename):
    return str(instance.author)+'/'+str(instance.timestamp).split()[0]+'/'+str(filename)

class Post(models.Model):
    author=models.ForeignKey(User,default=1)
    tags=models.CharField(max_length=150)
    title=models.CharField(max_length=120)
    timestamp=models.DateTimeField(auto_now_add=True)
    lyrics=models.CharField(max_length=300,null=True)
    artist=models.CharField(max_length=120)
    content=models.TextField(max_length=6000)
    image=models.ImageField(upload_to=location,blank=True)#Use of imagefield requires you to install pillow

    def __unicode__(self):
        return self.title+','+self.author

    def get_absolute_url(self):
        return reverse("posts:details",kwargs={"username":self.author,"id":self.id})