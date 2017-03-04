# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-16 00:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kolokwium', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValidChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolokwium.Choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolokwium.Question')),
            ],
        ),
        migrations.RenameModel(
            old_name='Answer',
            new_name='UserAnswer',
        ),
    ]
