# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-03 05:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20180303_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='publications',
        ),
        migrations.RenameField(
            model_name='abilitytraining',
            old_name='signup_user_list',
            new_name='volunteers',
        ),
        migrations.AlterField(
            model_name='campaignperson',
            name='campaign_person_user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campaignperson', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='volunteerinformation',
            name='volinfo_user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='平台用户'),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
    ]
