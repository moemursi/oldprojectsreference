# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-31 18:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0042_auto_20170328_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('EXAM_IDENTIFIED', 'Exame identificado'), ('ELIGIBLE_LAB', 'Laboratório elegível'), ('ALTERNATIVE_LAB_GIVEN', 'Laboratórios alternativos sugeridos'), ('PROCEDURES_NOT_COVERED', 'Exame não cobertos pelo Plano'), ('EXAM_TIME_SCHEDULED', 'Paciente agendou horário para o exame'), ('PATIENT_CANCELED', 'Paciente Cancelou'), ('LAB_RECORD_OPEN', 'Pré Cadastro criado no laboratório'), ('PROCEDURES_EXECUTED', 'Procedimento executado'), ('LAB_RECORD_CANCELED', 'Ficha no laboratório cancelada'), ('RESULTS_RECEIVED', 'Resultado do exame está pronto')], default='EXAM_IDENTIFIED', max_length=35)),
                ('scheduled_time', models.DateTimeField(blank=True, null=True)),
                ('procedure_average_duration', models.IntegerField(blank=True, null=True)),
                ('confirmation', models.BooleanField(default=False)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.Exam')),
                ('laboratory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='domain.Laboratory')),
            ],
        ),
        migrations.RemoveField(
            model_name='examresult',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='examresult',
            name='prescription',
        ),
        migrations.RemoveField(
            model_name='medicalprescription',
            name='confirmation',
        ),
        migrations.RemoveField(
            model_name='medicalprescription',
            name='exams',
        ),
        migrations.RemoveField(
            model_name='medicalprescription',
            name='lab_expected_time',
        ),
        migrations.RemoveField(
            model_name='medicalprescription',
            name='laboratory',
        ),
        migrations.RemoveField(
            model_name='medicalprescription',
            name='procedure_average_duration',
        ),
        migrations.RemoveField(
            model_name='medicalprescription',
            name='suggested_labs',
        ),
        migrations.AlterField(
            model_name='medicalprescription',
            name='status',
            field=models.CharField(choices=[('PATIENT_REQUESTED', 'Paciente submeteu pedido'), ('EXAMS_IDENTIFIED', 'Exames identificados')], default='PATIENT_REQUESTED', max_length=35),
        ),
        migrations.AddField(
            model_name='scheduledexam',
            name='prescription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.MedicalPrescription'),
        ),
        migrations.AddField(
            model_name='scheduledexam',
            name='suggested_labs',
            field=models.ManyToManyField(blank=True, related_name='suggested_labs', to='domain.Laboratory'),
        ),
        migrations.AddField(
            model_name='examresult',
            name='scheduled_exam',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='domain.ScheduledExam'),
            preserve_default=False,
        ),
    ]
