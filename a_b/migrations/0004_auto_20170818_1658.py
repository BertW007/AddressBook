# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-18 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_b', '0003_auto_20170817_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='type',
            field=models.CharField(max_length=32),
        ),
    ]