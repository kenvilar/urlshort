# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-11-30 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlshort',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='urlshort',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]