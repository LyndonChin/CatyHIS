# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FormGen', '0002_person_team_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.IntegerField(),
        ),
    ]
