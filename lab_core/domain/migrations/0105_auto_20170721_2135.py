# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-21 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0104_merge_20170717_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
