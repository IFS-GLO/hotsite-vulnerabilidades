# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-19 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20170921_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
