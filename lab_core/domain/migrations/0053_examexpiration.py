# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-10 16:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0052_auto_20170407_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamExpiration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration_in_days', models.IntegerField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.Exam')),
                ('insurance_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.InsuranceCompany')),
            ],
        ),
    ]