# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-02 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180203_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policyqa',
            name='qa_ask_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='提问时间'),
        ),
    ]
