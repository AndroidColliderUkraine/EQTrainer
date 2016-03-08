# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0022_auto_20160306_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlyreport',
            name='date_end',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='monthlyreport',
            name='date_start',
            field=models.DateField(null=True, blank=True),
        ),
    ]
