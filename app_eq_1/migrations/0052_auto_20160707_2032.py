# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0051_userprofile_subscribe_mailing'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='author',
            field=models.CharField(default=datetime.datetime(2016, 7, 7, 20, 32, 10, 46943, tzinfo=utc), help_text=b'Author of course (Denys Dubravin)', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.CharField(default=datetime.datetime(2016, 7, 7, 20, 32, 24, 711174, tzinfo=utc), help_text=b'Duration of course( 30 days)', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='time',
            field=models.CharField(default=datetime.datetime(2016, 7, 7, 20, 32, 28, 229925, tzinfo=utc), help_text=b'How many time user need to pass this course per day?(5 min/day)', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conclusions',
            name='courses',
            field=models.ManyToManyField(help_text=b'Recommended courses.', to='app_eq_1.Course', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='created',
            field=models.DateField(default=datetime.datetime(2016, 7, 7, 20, 32, 46, 834233, tzinfo=utc), help_text=b'Set date when does course created.'),
            preserve_default=False,
        ),
    ]
