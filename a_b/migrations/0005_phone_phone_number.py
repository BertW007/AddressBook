# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-18 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_b', '0004_auto_20170818_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
    ]