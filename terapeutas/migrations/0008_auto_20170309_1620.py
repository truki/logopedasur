# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-09 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terapeutas', '0007_auto_20170211_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terapeuta',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='terapeutas'),
        ),
    ]
