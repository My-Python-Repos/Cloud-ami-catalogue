# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 14:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ami',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ami_name', models.CharField(max_length=255)),
                ('ami_id', models.CharField(max_length=12)),
                ('platform', models.CharField(max_length=15)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2017, 8, 18, 14, 41, 2, 761118, tzinfo=utc))),
                ('end_of_life_date', models.DateTimeField(default=datetime.datetime(2017, 10, 17, 14, 41, 2, 761152, tzinfo=utc))),
                ('creator', models.CharField(default=b'CCOE - Hybrid Cloud Team', max_length=255)),
            ],
        ),
    ]
