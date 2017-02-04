# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-04 14:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_auto_20170204_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='class_assignments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('file', models.FileField(null=True, upload_to='resources/')),
                ('deadline', models.DateTimeField()),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.class_data')),
            ],
        ),
    ]
