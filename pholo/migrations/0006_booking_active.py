# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pholo', '0005_booking_product_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
