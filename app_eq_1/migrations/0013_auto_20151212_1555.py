# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0012_auto_20151212_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together=set([('number', 'course')]),
        ),
    ]
