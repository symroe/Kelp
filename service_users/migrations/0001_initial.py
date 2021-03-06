# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-03 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('contact_info', models.TextField(blank=True)),
                ('services', models.ManyToManyField(to='services.Service')),
            ],
        ),
    ]
