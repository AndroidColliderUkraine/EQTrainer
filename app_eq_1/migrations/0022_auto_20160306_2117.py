# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0021_auto_20160306_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklyreport',
            name='date_end',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='weeklyreport',
            name='date_start',
            field=models.DateField(null=True, blank=True),
        ),
    ]
