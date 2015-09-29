# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alexbook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alexbook',
            name='authors',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='num_pages',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='AlexBook',
        ),
    ]
