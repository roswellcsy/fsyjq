# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-17 02:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_auto_20180317_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='user_information_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='平台用户'),
        ),
    ]
