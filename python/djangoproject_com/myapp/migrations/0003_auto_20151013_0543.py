# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_person_custom_queryset'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person_custom_manager',
            new_name='PersonCustomManager',
        ),
        migrations.RenameModel(
            old_name='Person_custom_queryset',
            new_name='PersonCustomQuerySet',
        ),
    ]
