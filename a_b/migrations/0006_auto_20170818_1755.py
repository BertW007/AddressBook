# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-18 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_b', '0005_phone_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='phone_number',
            field=models.CharField(max_length=32),
        ),
    ]