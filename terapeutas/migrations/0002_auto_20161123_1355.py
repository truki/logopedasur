# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 13:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('terapeutas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='terapeuta',
            name='email',
        ),
        migrations.AddField(
            model_name='terapeuta',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='terapeutas'),
        ),
        migrations.AddField(
            model_name='terapeuta',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
