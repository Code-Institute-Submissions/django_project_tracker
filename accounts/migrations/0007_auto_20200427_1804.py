# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-04-27 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200426_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='favourite_games',
            field=models.TextField(blank=True, default='', max_length=200),
        ),
    ]