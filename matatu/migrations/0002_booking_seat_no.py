# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-03 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matatu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='seat_no',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
