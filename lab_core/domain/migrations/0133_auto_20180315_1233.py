# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-15 12:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0132_auto_20180302_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalprescription',
            name='preferred_date_to_schedule',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='medicalprescription',
            name='preferred_laboratory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='domain.Laboratory'),
        ),
    ]
