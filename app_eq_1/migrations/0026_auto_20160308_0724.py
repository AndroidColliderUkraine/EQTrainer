# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0025_weeklyreport_html'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyreport',
            name='html',
            field=models.TextField(help_text=b'Use in Email for Reports.', max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='weeklyreport',
            name='html',
            field=models.TextField(help_text=b'Use in Email for Reports.', max_length=5000, null=True),
        ),
    ]
