# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-22 15:23
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='active_end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='active_start_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 22, 15, 23, 15, 576108)),
            preserve_default=False,
        ),
    ]
