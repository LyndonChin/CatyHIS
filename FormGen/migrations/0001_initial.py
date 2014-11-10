# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.CharField(max_length=5)),
                ('team', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=10)),
                ('sex', models.CharField(max_length=2)),
                ('age', models.IntegerField()),
                ('community', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
