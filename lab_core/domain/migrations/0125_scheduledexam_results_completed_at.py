# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-07 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0124_auto_20171120_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduledexam',
            name='results_completed_at',
            field=models.DateTimeField(blank=True, db_index=True, default=None, null=True),
        ),
    ]
