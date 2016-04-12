# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-12 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miller', '0009_auto_20160411_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='snapshot',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='type',
            field=models.CharField(choices=[(b'bibtex', b'bibtex'), (b'video', b'video'), (b'picture', b'picture'), (b'pdf', b'pdf')], max_length=24),
        ),
    ]
