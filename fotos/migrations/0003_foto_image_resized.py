# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fotos', '0002_auto_20161102_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='image_resized',
            field=models.BooleanField(default=False),
        ),
    ]
