# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-19 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0019_auto_20170219_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pacientes.Tutor'),
        ),
    ]
