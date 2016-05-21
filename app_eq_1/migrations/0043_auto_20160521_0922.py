# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0042_auto_20160516_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default=b'avatars/default.png', upload_to=b'avatars', blank=True, help_text=b'Max 256 \xc3\x97 256', null=True),
        ),
    ]
