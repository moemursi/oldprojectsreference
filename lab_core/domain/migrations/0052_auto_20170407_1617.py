# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-07 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0051_auto_20170406_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='preferred_laboratory',
        ),
        migrations.AddField(
            model_name='patient',
            name='preferred_laboratories',
            field=models.ManyToManyField(blank=True, null=True, to='domain.Laboratory'),
        ),
    ]
