# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_eq_1', '0017_auto_20151219_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conclusions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emotion', models.CharField(max_length=50, null=True, choices=[(b'emotion_1', '\u0415\u043c\u043e\u0446\u0456\u044f_1'), (b'emotion_2', '\u0415\u043c\u043e\u0446\u0456\u044f_2'), (b'emotion_3', '\u0415\u043c\u043e\u0446\u0456\u044f_3'), (b'emotion_4', '\u0415\u043c\u043e\u0446\u0456\u044f_4'), (b'emotion_5', '\u0415\u043c\u043e\u0446\u0456\u044f_5'), (b'emotion_6', '\u0415\u043c\u043e\u0446\u0456\u044f_6'), (b'emotion_7', '\u0415\u043c\u043e\u0446\u0456\u044f_7'), (b'emotion_8', '\u0415\u043c\u043e\u0446\u0456\u044f_8'), (b'emotion_9', '\u0415\u043c\u043e\u0446\u0456\u044f_9'), (b'emotion_10', '\u0415\u043c\u043e\u0446\u0456\u044f_10')])),
                ('activity', models.CharField(max_length=50, null=True, choices=[(b'activity_1', '\u0410\u043a\u0442\u0438\u0432\u043d\u0456\u0441\u0442\u044c_1'), (b'activity_2', '\u0410\u043a\u0442\u0438\u0432\u043d\u0456\u0441\u0442\u044c_2'), (b'activity_3', '\u0410\u043a\u0442\u0438\u0432\u043d\u0456\u0441\u0442\u044c_3'), (b'activity_4', '\u0410\u043a\u0442\u0438\u0432\u043d\u0456\u0441\u0442\u044c_4'), (b'activity_5', '\u0410\u043a\u0442\u0438\u0432\u043d\u0456\u0441\u0442\u044c_5'), (b'activity_6', '\u0410\u043a\u0442\u0438\u0432\u043d\u0456\u0441\u0442\u044c_6'), (b'activity_7', '\u0410\u043a\u0442\u0438\u0432\u043d\u0456\u0441\u0442\u044c_7'), (b'activity_8', '\u0410\u043a\u0442\u0438\u0432\u043d\u0456\u0441\u0442\u044c_8')])),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='conclusions',
            unique_together=set([('emotion', 'activity')]),
        ),
    ]
