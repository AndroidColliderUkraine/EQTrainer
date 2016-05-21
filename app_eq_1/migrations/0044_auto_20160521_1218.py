# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0043_auto_20160521_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='text',
            field=models.TextField(help_text=b'You can use link in text: <a href="URL">...</a>', max_length=1024, null=True, blank=True),
        ),
    ]
