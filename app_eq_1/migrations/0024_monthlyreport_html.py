# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0023_auto_20160307_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlyreport',
            name='html',
            field=models.TextField(max_length=5000, null=True),
        ),
    ]
