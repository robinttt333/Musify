# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-24 09:31
from __future__ import unicode_literals

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20180524_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=posts.models.location),
        ),
    ]