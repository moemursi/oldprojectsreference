# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0005_auto_20161118_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalprescription',
            name='status',
            field=models.IntegerField(choices=[(1, 'Paciente submeteu pedido'), (2, 'Exames identificados'), (3, 'Laboratório elegível'), (4, 'Laboratórios alternativos sugeridos'), (5, 'Paciente Cancelou'), (6, 'Exames não cobertos pelo Plano'), (7, 'Pré Cadastro criado no laboratório'), (8, 'Procedimentos executaods')], default=1),
        ),
    ]