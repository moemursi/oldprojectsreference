# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-11 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0101_auto_20170704_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalprescription',
            name='annotations',
            field=models.TextField(blank=True, null=True),
        ),
    ]
