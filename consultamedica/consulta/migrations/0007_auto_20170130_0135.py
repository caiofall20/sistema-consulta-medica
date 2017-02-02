# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-30 04:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0006_auto_20170130_0056'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultaPaciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idconsulta', models.IntegerField()),
                ('horario_inicial', models.DateField(blank=True, null=True, verbose_name='Hora inicial')),
                ('horario_final', models.DateField(blank=True, null=True, verbose_name='Hora final')),
                ('cpfpaciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='consulta.Paciente')),
                ('crm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consulta.Medico')),
            ],
        ),
        migrations.RenameModel(
            old_name='Consulta',
            new_name='ConsultaMedico',
        ),
    ]
