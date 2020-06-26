# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 20:07
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slackdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slackuser',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='slackuser',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
