# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-12-01 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_auto_20181201_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshort',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
