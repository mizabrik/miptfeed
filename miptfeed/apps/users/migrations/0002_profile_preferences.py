# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='preferences',
            field=models.ManyToManyField(to='categories.Category'),
        ),
    ]
