# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0056_auto_20160930_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercourse',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 18, 25, 7, 451118, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
