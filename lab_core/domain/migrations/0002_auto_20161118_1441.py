# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 14:41
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaboratoryBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('is_active', models.BooleanField(default=False)),
                ('similar_brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='domain.LaboratoryBrand')),
            ],
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='medinc_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='medinc',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='id_dasa',
        ),
        migrations.RemoveField(
            model_name='laboratory',
            name='mnemonic',
        ),
        migrations.RemoveField(
            model_name='laboratory',
            name='status',
        ),
        migrations.AddField(
            model_name='exam',
            name='external_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='laboratory',
            name='external_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='laboratory',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
