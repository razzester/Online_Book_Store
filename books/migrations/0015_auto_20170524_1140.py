# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='features',
            field=models.ManyToManyField(blank=True, to='books.pop_features'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b'bk_img'),
        ),
    ]
