# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-12 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='books',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books', to='book_authors.Author'),
        ),
    ]
