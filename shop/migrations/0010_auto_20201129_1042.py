# Generated by Django 2.0.3 on 2020-11-29 02:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20201127_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 10, 42, 50, 414088), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 10, 42, 50, 414088), verbose_name='创建时间'),
        ),
    ]
