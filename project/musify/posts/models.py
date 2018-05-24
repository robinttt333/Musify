# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from persons.models import person
class Post(models.Model):
    author=models.ForeignKey(person)
    tags=models.CharField(max_length=150)
    title=models.CharField(max_length=120)
    timestamp=models.DateTimeField(auto_now_add=True)
    lyrics=models.CharField(max_length=300,null=True)
    artist=models.CharField(max_length=120)
    content=models.TextField(max_length=6000)
    def __unicode__(self):
        return self.title+','+self.author