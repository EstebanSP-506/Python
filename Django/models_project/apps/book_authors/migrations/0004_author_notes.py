# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-12 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0003_book_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
