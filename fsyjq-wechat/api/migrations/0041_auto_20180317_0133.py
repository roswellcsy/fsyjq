# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-16 17:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0040_auto_20180317_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='user_information_user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]