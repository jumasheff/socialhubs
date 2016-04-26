# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_objects', '0005_auto_20160426_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialhub',
            name='www',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='www'),
        ),
        migrations.AlterField(
            model_name='socialhub',
            name='address',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441'),
        ),
        migrations.AlterField(
            model_name='socialhub',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail'),
        ),
    ]
