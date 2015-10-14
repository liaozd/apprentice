# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100, null=True)),
                ('num_pages', models.IntegerField(null=True)),
                ('authors', models.ForeignKey(to='books.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
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
            name='person',
            unique_together=set([('first', 'last', 'middle')]),
        ),
    ]
