# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0023_auto_20161128_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalprescription',
            name='lab_expected_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
