# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20170524_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
