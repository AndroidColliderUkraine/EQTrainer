# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_eq_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmotionalState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fear', models.IntegerField(default=20)),
                ('confidence', models.IntegerField(default=20)),
                ('subjectivity', models.IntegerField(default=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('paid', models.BooleanField(default=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(to='app_eq_1.Course')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='emotional_state',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user_course',
            name='course',
        ),
        migrations.RemoveField(
            model_name='user_course',
            name='user',
        ),
        migrations.AlterField(
            model_name='action',
            name='user_course',
            field=models.ForeignKey(to='app_eq_1.UserCourse'),
        ),
        migrations.DeleteModel(
            name='Emotional_State',
        ),
        migrations.DeleteModel(
            name='User_Course',
        ),
    ]
