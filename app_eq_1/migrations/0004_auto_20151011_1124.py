# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0003_auto_20151005_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='video',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='photo',
            field=models.URLField(null=True, blank=True),
        ),
    ]
