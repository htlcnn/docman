# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0005_auto_20170325_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='collections',
            field=models.ManyToManyField(blank=True, null=True, to='doc.Collection', verbose_name='Tập hồ sơ'),
        ),
    ]
