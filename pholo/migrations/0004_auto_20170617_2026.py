# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pholo', '0003_auto_20170617_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pholo.Store'),
        ),
    ]
