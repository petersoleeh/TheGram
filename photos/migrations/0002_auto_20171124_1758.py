# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='photos.Comment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='post_img',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
    ]
