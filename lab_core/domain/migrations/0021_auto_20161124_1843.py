# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0020_auto_20161124_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratory',
            name='exams',
            field=models.ManyToManyField(blank=True, null=True, to='domain.Exam'),
        ),
    ]
