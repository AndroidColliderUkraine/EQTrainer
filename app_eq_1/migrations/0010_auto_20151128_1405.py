# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0009_monthlyreport_weeklyreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyreport',
            name='text',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='weeklyreport',
            name='text',
            field=models.TextField(max_length=5000, null=True),
        ),
    ]
