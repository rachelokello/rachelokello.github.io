# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 00:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=300, unique=True)),
                ('event_description', models.CharField(max_length=400)),
                ('event_image', models.ImageField(upload_to='')),
                ('event_details', models.TextField()),
                ('event_date', models.DateField()),
                ('event_status', models.CharField(choices=[('draft', 'draft'), ('published', 'published')], default='draft', max_length=12)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('event_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Executive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('executive_bio', models.CharField(max_length=500)),
                ('executive_picture', models.ImageField(upload_to='')),
                ('executive_position', models.CharField(max_length=200)),
                ('executive_qualification', models.CharField(max_length=10)),
                ('executive_gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=7)),
                ('executive_title', models.CharField(choices=[('Mr', 'Mr'), ('Miss', 'Miss'), ('Mrs', 'Mrs'), ('Dr', 'Dr'), ('Prof', 'Prof')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=300, unique=True)),
                ('news_description', models.CharField(max_length=400)),
                ('news_image_1', models.ImageField(upload_to='')),
                ('news_image_2', models.ImageField(blank=True, upload_to='')),
                ('news_image_3', models.ImageField(blank=True, upload_to='')),
                ('news_detail', models.TextField()),
                ('news_status', models.CharField(choices=[('draft', 'draft'), ('published', 'published')], default='draft', max_length=12)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('news_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=200)),
                ('school_logo', models.ImageField(upload_to='')),
                ('school_description', models.CharField(max_length=500)),
                ('school_address', models.CharField(max_length=400)),
                ('school_vision', models.TextField()),
                ('school_mission', models.TextField()),
                ('school_core_values', models.TextField()),
                ('phone_number_1', models.CharField(max_length=12)),
                ('phone_number_2', models.CharField(max_length=12)),
                ('email_address', models.EmailField(max_length=254)),
                ('email_address_2', models.EmailField(blank=True, max_length=254)),
                ('settings_status', models.CharField(choices=[('draft', 'draft'), ('published', 'published')], default='draft', max_length=12)),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('linkedin', models.URLField()),
                ('instagram', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('teachers_bio', models.CharField(max_length=500)),
                ('teachers_picture', models.ImageField(upload_to='')),
                ('teachers_qualification', models.CharField(max_length=10)),
                ('teachers_title', models.CharField(choices=[('Mr', 'Mr'), ('Miss', 'Miss'), ('Mrs', 'Mrs'), ('Dr', 'Dr'), ('Prof', 'Prof')], max_length=7)),
                ('teachers_gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=7)),
                ('teachers_status', models.CharField(choices=[('draft', 'draft'), ('published', 'published')], default='draft', max_length=10)),
                ('teachers_email', models.EmailField(max_length=254)),
                ('teachers_phone', models.CharField(max_length=13)),
            ],
        ),
    ]