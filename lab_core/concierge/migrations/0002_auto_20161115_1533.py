# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 15:33
from __future__ import unicode_literals

from django.db import migrations, models

import concierge.models


class Migration(migrations.Migration):

    dependencies = [
        ('concierge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=concierge.models.operator_upload),
        ),
    ]