# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-18 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=250, primary_key=True, serialize=False, unique=True),
        ),
    ]
