# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-13 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0012_auto_20170210_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='cod_postal',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='tutor',
            name='localidad',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
