# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-24 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0060_auto_20170424_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratoryopeninghours',
            name='closes_at',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='laboratoryopeninghours',
            name='opens_at',
            field=models.TimeField(blank=True, null=True),
        ),
    ]