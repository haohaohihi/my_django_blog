# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-17 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='名称')),
                ('url', models.URLField(default='', verbose_name='链接')),
            ],
        ),
    ]
