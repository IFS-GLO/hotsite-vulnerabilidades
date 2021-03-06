# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_vulnerability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vulnerability',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='vulnerability',
            name='detected_at',
            field=models.DateField(verbose_name='Detectado em'),
        ),
        migrations.AlterField(
            model_name='vulnerability',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Atualizado em'),
        ),
    ]
