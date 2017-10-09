# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-10-09 16:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_auto_20171009_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duelisttournament',
            name='duelist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='duelistTournaments', to='cms.Duelist', verbose_name='\u53c2\u52a0\u8005'),
        ),
        migrations.AlterField(
            model_name='duelisttournament',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='duelistTournaments', to='cms.Tournament', verbose_name='\u5927\u4f1a'),
        ),
    ]
