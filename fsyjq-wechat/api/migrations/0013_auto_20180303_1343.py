# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-03 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20180303_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='user_information_volunteer',
            field=models.BooleanField(default=False, verbose_name='是否志愿者'),
        ),
    ]
