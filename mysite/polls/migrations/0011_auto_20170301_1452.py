# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_remove_event_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=50)),
                ('vender_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='isFinal',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer_name',
            field=models.CharField(default=b'admin', max_length=50),
        ),
        migrations.AlterField(
            model_name='answer',
            name='comment',
            field=models.CharField(default=b'none', max_length=200),
        ),
        migrations.AddField(
            model_name='vender',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Event'),
        ),
        migrations.AddField(
            model_name='vender',
            name='vender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.User'),
        ),
    ]