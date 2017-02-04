# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-04 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_subjects_announcements'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects_assignments',
            name='file',
            field=models.FileField(null=True, upload_to='resources/'),
        ),
        migrations.AlterField(
            model_name='subjects_resources',
            name='file',
            field=models.FileField(null=True, upload_to='resources/'),
        ),
    ]
