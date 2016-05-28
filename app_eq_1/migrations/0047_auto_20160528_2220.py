# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0046_course_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created',
            field=models.DateTimeField(help_text=b'Set date when does course created.', null=True, blank=True),
        ),
    ]
