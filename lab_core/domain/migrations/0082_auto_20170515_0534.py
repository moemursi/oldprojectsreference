# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-15 05:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0081_auto_20170515_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preparationstep',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
