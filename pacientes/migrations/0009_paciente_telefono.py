# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-31 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0008_paciente_tutor'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='telefono',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]