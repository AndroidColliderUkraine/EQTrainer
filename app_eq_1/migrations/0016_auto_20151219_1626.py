# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0015_article_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='content',
        ),
        migrations.AddField(
            model_name='article',
            name='short_text',
            field=redactor.fields.RedactorField(default=datetime.datetime(2015, 12, 19, 16, 26, 48, 984479, tzinfo=utc), verbose_name='Text'),
            preserve_default=False,
        ),
    ]
