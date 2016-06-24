# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0048_auto_20160528_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price_dol',
            field=models.IntegerField(default=0, help_text=b'Price in US dollars.'),
        ),
        migrations.AddField(
            model_name='course',
            name='price_rub',
            field=models.IntegerField(default=0, help_text=b'Price in rubles.'),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.IntegerField(default=0, help_text=b'Price of Ukrainian hryvnia.'),
        ),
    ]
