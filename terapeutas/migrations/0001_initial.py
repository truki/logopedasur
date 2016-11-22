# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Terapeuta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('apellidos', models.CharField(max_length=256)),
                ('dni', models.CharField(max_length=9, unique=True)),
                ('direccion', models.CharField(max_length=256)),
                ('cod_postal', models.DecimalField(decimal_places=0, max_digits=5)),
                ('localidad', models.CharField(blank=True, max_length=128)),
                ('provincia', models.CharField(blank=True, max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('seg_social', models.CharField(blank=True, default='', max_length=12)),
            ],
        ),
    ]