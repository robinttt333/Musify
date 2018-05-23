# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class person(models.Model):
    username=models.CharField(max_length=120)

    def __unicode__(self):
        return self.username