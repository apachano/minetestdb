# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 20:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mods', '0002_auto_20170808_1311'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servers', '0002_server_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('notifications', models.ManyToManyField(blank=True, to='users.Notification', verbose_name='Notification')),
                ('stared_mods', models.ManyToManyField(blank=True, to='mods.Mod', verbose_name='Mods')),
                ('stared_servers', models.ManyToManyField(blank=True, to='servers.Server', verbose_name='Servers')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
