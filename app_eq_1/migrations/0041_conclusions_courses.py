# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0027_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='conclusions',
            name='courses',
            field=models.ManyToManyField(help_text=b'Recommended courses.', to='app_eq_1.Course', null=True),
        ),
    ]
