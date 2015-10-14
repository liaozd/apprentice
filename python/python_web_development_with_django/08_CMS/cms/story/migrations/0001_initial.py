# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=50, blank=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('markdown_content', models.TextField()),
                ('html_content', models.TextField(editable=False)),
                ('status', models.IntegerField(default=1, choices=[(1, b'Needs Edit'), (2, b'Needs Approval'), (3, b'Published'), (4, b'Archieved')])),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('modified', models.DateTimeField(default=datetime.datetime.now)),
                ('category', models.ForeignKey(to='story.Category')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['modified'],
                'verbose_name_plural': 'stories',
            },
        ),
    ]
