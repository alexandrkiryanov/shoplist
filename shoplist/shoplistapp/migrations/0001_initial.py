# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 18:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ShopListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=200)),
                ('itemChecked', models.BooleanField()),
                ('shopList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoplistapp.ShopList')),
            ],
        ),
    ]
