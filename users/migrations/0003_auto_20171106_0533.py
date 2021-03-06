# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 05:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171106_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.IntegerField(choices=[(0, 'currently a primary school pupil'), (1, 'primary school'), (2, 'secondary school'), (3, 'college/bachelor degree'), (4, 'masters degree'), (5, 'doctorate degree')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('F', 'female'), ('M', 'male')], max_length=1),
        ),
    ]
