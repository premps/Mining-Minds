# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 06:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_visit', models.IntegerField(blank=True, null=True)),
                ('action_name', models.CharField(blank=True, max_length=50)),
                ('entry_screen', models.CharField(blank=True, max_length=50)),
                ('exit_screen', models.CharField(blank=True, max_length=50)),
                ('visit_time', models.DateTimeField(blank=True, null=True)),
                ('first_visit_timestamp', models.BigIntegerField(blank=True, null=True)),
                ('prevoius_visit_timestamp', models.BigIntegerField(blank=True, null=True)),
                ('screen_resolution', models.CharField(blank=True, max_length=70)),
                ('user_agent', models.CharField(blank=True, max_length=70)),
                ('language', models.CharField(blank=True, max_length=7)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('event_category', models.CharField(blank=True, max_length=70)),
                ('event_name', models.CharField(blank=True, max_length=70)),
                ('event_action', models.CharField(blank=True, max_length=70)),
                ('event_value', models.CharField(blank=True, max_length=70)),
                ('total_events', models.IntegerField(blank=True, null=True)),
                ('total_number_of_visit', models.IntegerField(blank=True, null=True)),
                ('actionlog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='analytics.ActionLog')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytics.App')),
                ('appuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.MyUser')),
            ],
        ),
    ]