# Generated by Django 2.2.3 on 2019-07-09 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20190705_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.TypeUse', verbose_name='Tipo de uso'),
        ),
    ]