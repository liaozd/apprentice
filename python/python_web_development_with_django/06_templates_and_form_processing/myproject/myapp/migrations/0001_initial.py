# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first', models.CharField(max_length=100)),
                ('last', models.CharField(max_length=100)),
                ('middle', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'ordering': ['last', 'first', 'middle'],
                'verbose_name_plural': 'people',
            },
        ),
        migrations.AlterUniqueTogether(
            name='people',
            unique_together=set([('first', 'last', 'middle')]),
        ),
    ]
