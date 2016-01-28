# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0018_auto_20160128_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='conclusions',
            name='text',
            field=models.TextField(default=datetime.datetime(2016, 1, 28, 20, 55, 22, 224577, tzinfo=utc), max_length=5000),
            preserve_default=False,
        ),
    ]
