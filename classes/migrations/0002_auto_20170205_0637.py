# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-05 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class_announcements',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='resources/'),
        ),
        migrations.AlterField(
            model_name='class_assignments',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='resources/'),
        ),
    ]
