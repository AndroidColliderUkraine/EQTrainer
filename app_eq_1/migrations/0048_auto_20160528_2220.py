# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0047_auto_20160528_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created',
            field=models.DateField(help_text=b'Set date when does course created.', null=True, blank=True),
        ),
    ]
