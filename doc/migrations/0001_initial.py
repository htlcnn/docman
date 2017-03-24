# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 23:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Tên')),
                ('summary', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Tập hồ sơ',
                'verbose_name_plural': 'Tập hồ sơ',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=250, verbose_name='Số văn bản')),
                ('date', models.DateField(verbose_name='Ngày')),
                ('summary', models.TextField(verbose_name='Trích yếu')),
                ('issued_by', models.CharField(max_length=250, verbose_name='Nơi ban hành')),
                ('collections', models.ManyToManyField(to='doc.Collection', verbose_name='Tập hồ sơ')),
            ],
            options={
                'verbose_name': 'Tài liệu',
                'verbose_name_plural': 'Tài liệu',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Tên dự án')),
                ('investor', models.CharField(max_length=250, verbose_name='Chủ đầu tư')),
                ('location', models.CharField(max_length=250, verbose_name='Địa điểm')),
                ('total_investment', models.CharField(max_length=20, verbose_name='Tổng mức đầu tư')),
                ('equity_source', models.CharField(max_length=250, verbose_name='Nguồn vốn')),
                ('time', models.CharField(max_length=250, verbose_name='Thời gian thực hiện')),
            ],
            options={
                'verbose_name': 'Dự án',
                'verbose_name_plural': 'Dự án',
            },
        ),
        migrations.CreateModel(
            name='SaveLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='doc.SaveLocation')),
            ],
            options={
                'verbose_name': 'Nơi lưu',
                'verbose_name_plural': 'Nơi lưu',
            },
        ),
        migrations.AddField(
            model_name='document',
            name='projects',
            field=models.ManyToManyField(to='doc.Project', verbose_name='Dự án'),
        ),
        migrations.AddField(
            model_name='collection',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.SaveLocation', verbose_name='Nơi lưu'),
        ),
    ]
