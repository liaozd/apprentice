# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20150928_0030'),
    ]

    operations = [
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
