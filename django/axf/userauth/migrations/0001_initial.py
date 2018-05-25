# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-08 01:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0004_remove_usermodel_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.CharField(max_length=255)),
                ('out_time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.UserModel')),
            ],
            options={
                'db_table': 'user_cookie',
            },
        ),
    ]