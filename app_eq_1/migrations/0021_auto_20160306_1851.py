# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0020_auto_20160306_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklyreport',
            name='date_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='weeklyreport',
            name='date_start',
            field=models.DateField(),
        ),
    ]
