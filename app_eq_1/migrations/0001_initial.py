# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500, null=True, blank=True)),
                ('tags', models.CharField(max_length=500, null=True, blank=True)),
                ('headline', models.TextField(max_length=120, null=True, blank=True)),
                ('text', models.TextField(max_length=120, null=True, blank=True)),
                ('photo', models.URLField(null=True, verbose_name=b'Photo', blank=True)),
                ('state', models.CharField(default=b'not_active', max_length=20, null=True, choices=[(b'active', b'\xd0\x90\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd0\xb0'), (b'not_active', b'\xd0\x9d\xd0\xb5 \xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd0\xb0')])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500, null=True, blank=True)),
                ('tags', models.CharField(max_length=500, null=True, blank=True)),
                ('text', models.TextField(max_length=120, null=True, blank=True)),
                ('photo', models.URLField(null=True, verbose_name=b'Photo', blank=True)),
                ('state', models.CharField(default=b'not_active', max_length=20, null=True, choices=[(b'active', b'\xd0\x90\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd0\xb0'), (b'not_active', b'\xd0\x9d\xd0\xb5 \xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd0\xb0')])),
                ('price', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Emotional_State',
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
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500, null=True, blank=True)),
                ('tags', models.CharField(max_length=500, null=True, blank=True)),
                ('text', models.TextField(max_length=120, null=True, blank=True)),
                ('number', models.IntegerField(unique=True)),
                ('state', models.CharField(default=b'not_active', max_length=20, null=True, choices=[(b'active', b'\xd0\x90\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd0\xb0'), (b'not_active', b'\xd0\x9d\xd0\xb5 \xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd0\xb0')])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(to='app_eq_1.Course')),
            ],
        ),
        migrations.CreateModel(
            name='User_Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('paid', models.BooleanField(default=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(to='app_eq_1.Course')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='action',
            name='lesson',
            field=models.ForeignKey(to='app_eq_1.Lesson'),
        ),
        migrations.AddField(
            model_name='action',
            name='user_course',
            field=models.ForeignKey(to='app_eq_1.User_Course'),
        ),
    ]
