# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 14:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ami_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ami',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 18, 14, 41, 5, 686147, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ami',
            name='end_of_life_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 17, 14, 41, 5, 686185, tzinfo=utc)),
        ),
    ]
