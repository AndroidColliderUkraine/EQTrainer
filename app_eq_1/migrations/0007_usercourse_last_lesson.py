# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0006_usercourse_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercourse',
            name='last_lesson',
            field=models.IntegerField(default=0),
        ),
    ]
