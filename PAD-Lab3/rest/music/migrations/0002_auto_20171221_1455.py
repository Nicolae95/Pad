# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-12-21 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='album',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='music',
            name='singer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
