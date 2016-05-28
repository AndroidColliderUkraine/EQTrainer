# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0045_auto_20160521_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
