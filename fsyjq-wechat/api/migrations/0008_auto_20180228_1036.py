# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-28 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20180228_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policyqa',
            name='qa_type',
            field=models.CharField(blank=True, choices=[('1', '居住证及相关'), ('2', '户籍及相关'), ('3', '计生及相关'), ('4', '住房及相关'), ('5', '子女教育及相关'), ('6', '积分制及相关')], max_length=1, null=True, verbose_name='类型'),
        ),
    ]
