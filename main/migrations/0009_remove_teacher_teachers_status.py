# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 10:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20171004_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='teachers_status',
        ),
    ]
