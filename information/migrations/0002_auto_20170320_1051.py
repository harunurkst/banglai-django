# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 10:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='districts',
            old_name='division_name',
            new_name='division',
        ),
    ]