# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-14 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('terapeutas', '0007_auto_20170211_1119'),
        ('pacientes', '0015_auto_20170213_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Informe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=256, null=True)),
                ('fecha_informe', models.DateField(blank=True, null=True)),
                ('fecha_modificacion', models.DateField()),
                ('fichero', models.FileField(blank=True, null=True, upload_to='pacientes/uploads/%Y/%m/%d/')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.Paciente')),
                ('terapeutas', models.ManyToManyField(to='terapeutas.Terapeuta')),
            ],
        ),
    ]