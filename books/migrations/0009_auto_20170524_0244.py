# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20170524_0240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='id',
        ),
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
