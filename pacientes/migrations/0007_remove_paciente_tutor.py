# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-31 07:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0006_auto_20170131_0705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='tutor',
        ),
    ]
