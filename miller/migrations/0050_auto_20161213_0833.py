# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miller', '0049_review_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='thematic',
            field=models.TextField(blank=True, null=True),
        ),
    ]
