# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 10:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20171003_2238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='executive',
            old_name='excutive_religion',
            new_name='executive_religion',
        ),
    ]