# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-04 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_teachers_data_otp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachers_data',
            name='roll_no',
        ),
        migrations.AlterField(
            model_name='teachers_data',
            name='id',
            field=models.CharField(max_length=120, primary_key=True, serialize=False),
        ),
    ]
