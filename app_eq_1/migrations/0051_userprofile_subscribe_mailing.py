# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0050_auto_20160702_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='subscribe_mailing',
            field=models.BooleanField(default=True),
        ),
    ]
