# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0003_auto_20161121_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='pacientes'),
        ),
    ]