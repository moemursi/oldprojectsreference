# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-20 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0119_auto_20170918_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratorybrand',
            name='premium',
            field=models.BooleanField(default=False),
        ),
    ]
