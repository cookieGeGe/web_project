# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-16 12:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pro_img', models.CharField(max_length=50)),
                ('pro_desc', models.TextField(max_length=255)),
                ('last_num', models.IntegerField(max_length=11)),
                ('sale_num', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'day_goods',
            },
        ),
        migrations.CreateModel(
            name='ProductClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=200)),
                ('c_desc', models.TextField()),
                ('c_img', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'day_pro_class',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='class_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.ProductClass'),
        ),
    ]