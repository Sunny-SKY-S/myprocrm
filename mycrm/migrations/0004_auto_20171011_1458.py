# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-11 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycrm', '0003_auto_20171010_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='menu',
        ),
        migrations.AddField(
            model_name='role',
            name='menu',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]