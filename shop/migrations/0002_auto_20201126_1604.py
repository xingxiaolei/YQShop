# Generated by Django 2.0.3 on 2020-11-26 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': '轮播图管理', 'verbose_name_plural': '轮播图管理'},
        ),
        migrations.AlterField(
            model_name='banner',
            name='name',
            field=models.CharField(max_length=10, verbose_name='轮播图名称'),
        ),
        migrations.AlterModelTable(
            name='banner',
            table='banner',
        ),
    ]
