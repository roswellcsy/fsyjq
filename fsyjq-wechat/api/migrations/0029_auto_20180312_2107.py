# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-12 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_remove_volunteerinformation_volinfo_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteerinformation',
            name='volinfo_age',
        ),
        migrations.AlterField(
            model_name='policyqa',
            name='qa_sex',
            field=models.CharField(choices=[('1', '男'), ('2', '女')], default=1, max_length=1, verbose_name='性别'),
        ),
    ]
