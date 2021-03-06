# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-01 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180302_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='campaign_certified_hours',
            field=models.PositiveIntegerField(default=0, verbose_name='志愿活动认证时数'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='campaign_counts',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='可报名总人数'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='campaign_vol_counts',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='可报名志愿者人数'),
        ),
    ]
