# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-25 09:37
from __future__ import unicode_literals

from django.db import migrations, models
import miller.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('miller', '0032_document_mimetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='mimetype',
            field=models.CharField(blank=True, default=b'', max_length=127),
        ),
        migrations.AlterField(
            model_name='document',
            name='short_url',
            field=models.CharField(blank=True, db_index=True, default=miller.helpers.create_short_url, max_length=22, unique=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='slug',
            field=models.CharField(blank=True, max_length=150, unique=True),
        ),
    ]