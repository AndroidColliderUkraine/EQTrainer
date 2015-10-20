# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0004_auto_20151011_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='date',
        ),
        migrations.RemoveField(
            model_name='article',
            name='date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='date',
        ),
        migrations.RemoveField(
            model_name='emotionalstate',
            name='date',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='date',
        ),
        migrations.RemoveField(
            model_name='usercourse',
            name='date',
        ),
        migrations.AddField(
            model_name='course',
            name='icon',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='small_photo',
            field=models.URLField(null=True, blank=True),
        ),
    ]
