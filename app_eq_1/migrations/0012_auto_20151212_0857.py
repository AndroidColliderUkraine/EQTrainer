# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0011_training'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monthlyreport',
            name='date',
        ),
        migrations.RemoveField(
            model_name='training',
            name='date',
        ),
        migrations.RemoveField(
            model_name='weeklyreport',
            name='date',
        ),
        migrations.AddField(
            model_name='action',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='emotionalstate',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lesson',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='monthlyreport',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='monthlyreport',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 12, 8, 57, 16, 921579, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='training',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='training',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 12, 8, 57, 27, 463770, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usercourse',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='weeklyreport',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='weeklyreport',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 12, 8, 57, 33, 590682, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emotionalstate',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
