# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-06 14:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_publisher_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Publisher',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
