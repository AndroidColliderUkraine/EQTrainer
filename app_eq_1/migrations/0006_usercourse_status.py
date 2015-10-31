# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0005_auto_20151018_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercourse',
            name='status',
            field=models.CharField(default=b'begin', max_length=20, null=True, choices=[(b'begin', b'\xd0\x9f\xd0\xbe\xd1\x87\xd0\xb0\xd1\x82\xd0\xba\xd0\xbe\xd0\xb2\xd0\xb8\xd0\xb9'), (b'active', b'\xd0\x90\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbe\xd0\xbd\xd0\xb8\xd0\xb9'), (b'ended', b'\xd0\x97\xd0\xb0\xd0\xb2\xd0\xb5\xd1\x80\xd1\x88\xd0\xb8\xd0\xbd\xd0\xb8\xd0\xb9')]),
        ),
    ]
