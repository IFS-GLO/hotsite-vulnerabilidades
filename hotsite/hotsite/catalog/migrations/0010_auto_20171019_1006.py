# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-19 13:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20170905_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Tipo de uso',
                'verbose_name_plural': 'Tipo de uso',
            },
        ),
        migrations.AddField(
            model_name='vulnerability',
            name='has_kaspersky',
            field=models.BooleanField(default=False, verbose_name='Está no catálogo da Kaspersky?'),
        ),
    ]
