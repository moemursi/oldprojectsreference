# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 14:51
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0002_auto_20161118_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratory',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='domain.LaboratoryBrand'),
        ),
    ]
