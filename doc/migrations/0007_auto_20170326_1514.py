# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0006_auto_20170326_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='collections',
            field=models.ManyToManyField(blank=True, to='doc.Collection', verbose_name='Tập hồ sơ'),
        ),
        migrations.AlterField(
            model_name='document',
            name='projects',
            field=models.ManyToManyField(blank=True, to='doc.Project', verbose_name='Dự án'),
        ),
    ]
