# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0002_doc_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='no',
            field=models.CharField(max_length=250, verbose_name='Số văn bản'),
        ),
    ]
