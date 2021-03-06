# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-30 20:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0007_auto_20170130_0135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idconsulta', models.IntegerField()),
                ('horario_inicial', models.DateTimeField(auto_now_add=True)),
                ('horario_final', models.DateTimeField(auto_now_add=True)),
                ('cpfpaciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='consulta.Paciente')),
                ('crm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consulta.Medico')),
            ],
        ),
        migrations.RemoveField(
            model_name='consultamedico',
            name='cpfpaciente',
        ),
        migrations.RemoveField(
            model_name='consultamedico',
            name='crm',
        ),
        migrations.RemoveField(
            model_name='consultapaciente',
            name='cpfpaciente',
        ),
        migrations.RemoveField(
            model_name='consultapaciente',
            name='crm',
        ),
        migrations.DeleteModel(
            name='ConsultaMedico',
        ),
        migrations.DeleteModel(
            name='ConsultaPaciente',
        ),
    ]
