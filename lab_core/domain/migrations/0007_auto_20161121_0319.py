# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0006_auto_20161118_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalprescription',
            name='status',
            field=models.CharField(choices=[('PATIENT_REQUESTED', 'Paciente submeteu pedido'), ('EXAMS_IDENTIFIED', 'Exames identificados'), ('ELIGIBLE_LAB', 'Laboratório elegível'), ('ALTERNATIVE_LAB_GIVEN', 'Laboratórios alternativos sugeridos'), ('PATIENT_CANCELED', 'Paciente Cancelou'), ('PROCEDURES_NOT_COVERED', 'Exames não cobertos pelo Plano'), ('LAB_RECORD_OPEN', 'Pré Cadastro criado no laboratório'), ('PROCEDURES_EXECUTED', 'Procedimentos executaods')], default='PATIENT_REQUESTED', max_length=35),
        ),
    ]
