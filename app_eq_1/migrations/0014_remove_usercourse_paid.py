# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0013_auto_20151212_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercourse',
            name='paid',
        ),
    ]
