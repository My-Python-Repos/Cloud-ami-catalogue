# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-14 23:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ami_info', '0006_auto_20170823_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ami',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 14, 23, 12, 39, 605000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ami',
            name='end_of_life_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 13, 23, 12, 39, 605032, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='update',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 14, 23, 12, 39, 611951, tzinfo=utc)),
        ),
    ]
