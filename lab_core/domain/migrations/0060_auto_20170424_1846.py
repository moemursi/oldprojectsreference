# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-24 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0059_laboratoryopeninghours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratoryopeninghours',
            name='week_day',
            field=models.CharField(choices=[('Dom', 'Domingo'), ('Seg', 'Segunda-feira'), ('Seg', 'Terça-feira'), ('Seg', 'Quarta-feira'), ('Seg', 'Quinta-feira'), ('Seg', 'Sexta-feira'), ('Seg', 'Sábado')], max_length=3),
        ),
    ]
