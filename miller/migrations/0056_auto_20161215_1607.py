# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miller', '0055_auto_20161215_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='status',
            field=models.CharField(choices=[(b'initial', b'initial'), (b'draft', b'draft'), (b'private', b'private'), (b'public', b'public'), (b'refusal', b'refusal'), (b'bounce', b'bounce'), (b'complete', b'complete')], default=b'initial', max_length=8),
        ),
    ]