# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0003_auto_20170125_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='horario_final',
            field=models.DateField(null=True, verbose_name=b'Hora final', blank=True),
        ),
        migrations.AddField(
            model_name='consulta',
            name='horario_inicial',
            field=models.DateField(null=True, verbose_name=b'Hora inicial', blank=True),
        ),
    ]
