# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-12 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0002_auto_20180412_0506'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]
