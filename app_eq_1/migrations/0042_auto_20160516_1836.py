# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0041_conclusions_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='small_photo',
        ),
        migrations.AlterField(
            model_name='course',
            name='icon',
            field=models.URLField(help_text=b'PNG, 192 \xc3\x97 192.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='photo',
            field=models.URLField(help_text=b'Recommended size: 1024 \xc3\x97 768.', null=True, blank=True),
        ),
    ]
