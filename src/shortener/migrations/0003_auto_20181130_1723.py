# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-11-30 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20181130_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshort',
            name='shortcode',
            field=models.CharField(blank=True, default='abc', max_length=15, unique=True),
        ),
    ]