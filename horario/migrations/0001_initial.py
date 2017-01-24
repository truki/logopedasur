# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 07:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('terapeutas', '0005_auto_20161213_0703'),
        ('pacientes', '0005_sesion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora_ini', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.Paciente')),
                ('terapeutas', models.ManyToManyField(to='terapeutas.Terapeuta')),
            ],
        ),
    ]