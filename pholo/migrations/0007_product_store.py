# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 23:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pholo', '0006_booking_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pholo.Store'),
        ),
    ]
