# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-08-30 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='doc',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='帮助文档'),
        ),
    ]