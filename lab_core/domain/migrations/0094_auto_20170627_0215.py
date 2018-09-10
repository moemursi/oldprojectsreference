# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-27 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0093_auto_20170627_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledexam',
            name='status',
            field=models.CharField(choices=[('EXAM_IDENTIFIED', 'Exame identificado'), ('ELIGIBLE_PATIENT', 'Paciente elegível'), ('NOT_ELIGIBLE_PATIENT_DUE_TO_AGE_OR_GENDER', 'Paciente não elegível por questão de idade ou sexo'), ('PROCEDURES_NOT_COVERED', 'Exame não cobertos pelo Plano ou laboratório não executa o exame'), ('ALTERNATIVE_LAB_GIVEN', 'Laboratórios alternativos sugeridos'), ('PHONE_CALL_SCHEDULED', 'Ligação telefônica agendada'), ('EXAM_TIME_SCHEDULED', 'Paciente agendou horário para o exame'), ('PHONE_CALL_NOT_ANSWERED', 'Ligação telefônica não atendida'), ('PATIENT_CANCELED_BY_CALL', 'Paciente cancelou o exame pela ligação telefônica'), ('PATIENT_CANCELED', 'Paciente Cancelou'), ('EXAM_MISSED', 'Exame estava agendado mas o paciente não compareceu'), ('LAB_RECORD_OPEN', 'Pré Cadastro criado no laboratório'), ('PROCEDURES_EXECUTED', 'Procedimento executado'), ('LAB_RECORD_CANCELED', 'Ficha no laboratório cancelada'), ('RESULTS_DELAYED', 'Resultados do exame estão atrasados'), ('RESULTS_RECEIVED', 'Resultado do exame está pronto')], db_index=True, default='EXAM_IDENTIFIED', max_length=150),
        ),
        migrations.AlterIndexTogether(
            name='scheduledexam',
            index_together=set([('scheduled_time', 'status'), ('exam', 'status'), ('prescription', 'status'), ('laboratory', 'prescription')]),
        ),
    ]
