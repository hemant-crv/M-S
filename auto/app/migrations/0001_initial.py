# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('emplyee_id', models.IntegerField()),
                ('project', models.CharField(max_length=250)),
                ('position', models.CharField(max_length=250)),
                ('duration', models.IntegerField()),
                ('access', models.CharField(max_length=250)),
            ],
        ),
    ]
