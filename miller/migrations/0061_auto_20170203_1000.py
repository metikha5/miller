# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-03 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miller', '0060_auto_20170201_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='category',
            field=models.CharField(choices=[(b'keyword', b'keyword'), (b'blog', b'blog'), (b'highlights', b'highlights'), (b'writing', b'writing'), (b'collection', b'collection'), (b'publishing', b'publishing')], default=b'keyword', max_length=32),
        ),
    ]
