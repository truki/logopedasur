# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 21:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terapeutas', '0002_auto_20161123_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terapeuta',
            name='direccion',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]