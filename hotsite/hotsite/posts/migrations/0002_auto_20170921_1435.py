# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='C:\\wamp64\\www\\ifs\\vulnerabilidades\\hotsite\\hotsite\\core\\media', verbose_name='Imagem Destacada'),
        ),
    ]
