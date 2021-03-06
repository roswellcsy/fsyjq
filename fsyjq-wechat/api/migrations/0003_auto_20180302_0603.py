# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-01 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180302_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='campaign_certified_hours',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='志愿活动认证时数'),
        ),
        migrations.AddField(
            model_name='volunteerinformation',
            name='volinfo_service_time',
            field=models.PositiveIntegerField(default=0, verbose_name='志愿活动认证时数'),
        ),
    ]
