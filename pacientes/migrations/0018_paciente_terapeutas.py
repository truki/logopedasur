# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-19 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terapeutas', '0007_auto_20170211_1119'),
        ('pacientes', '0017_auto_20170216_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='terapeutas',
            field=models.ManyToManyField(to='terapeutas.Terapeuta'),
        ),
    ]
