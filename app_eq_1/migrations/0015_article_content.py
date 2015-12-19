# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0014_remove_usercourse_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(default=datetime.datetime(2015, 12, 19, 14, 28, 19, 861859, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
