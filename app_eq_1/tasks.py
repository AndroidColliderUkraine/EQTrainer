#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from celery import task
from app_eq_1.models import UserCourse
from app_eq_1.models import Lesson
from app_eq_1.models import Action
from django.contrib.auth.models import User
import datetime


@task()
def example():
    print '[ EVERY_30_SECONDS ] [ %s ]' % (str(datetime.datetime.now().time()),)


@task()
def every_day():
    print '[ EVERY_DAY ] [ %s ]' % (str(datetime.datetime.now().time()),)

    try:
        for item in UserCourse.objects.filter(deleted=False).filter(status='active').distinct():
            try:
                if item.last_lesson < item.course.lesson_set.count():
                    action_new = Action(user_course=item,
                                        lesson=item.course.lesson_set.get(number=item.last_lesson + 1))
                    action_new.save()

                    item.last_lesson += 1
                    item.save()
                    send_email(item.course.lesson_set.get(number=item.last_lesson).id, item.user.id)
                else:
                    item.status = 'ended'
                    item.save()
            except Exception, e:
                print e
    except Exception, e:
        print e


@task()
def every_week():
    print '[ EVERY_WEEK ] [ %s ]' % (str(datetime.datetime.now().time()),)
    try:

        EMAIL_SUBJECT = 'TEST EMAIL'
        EMAIL_MESSAGE = u'Привіт усім, це перевірка роботи щотижневого звіту.'
        EMAIL_EMAIL_FROM = 'eq@eq.com'
        EMAIL_EMAIL_TO = 'tarasinf2013@gmail.com'

        from django.core.mail import send_mail
        send_mail(EMAIL_SUBJECT, EMAIL_MESSAGE, EMAIL_EMAIL_FROM, [EMAIL_EMAIL_TO], fail_silently=False)
    except Exception, e:
        print '[send_email]', e

@task
def every_month():
    print '[ EVERY_MONTH ] [ %s ]' % (str(datetime.datetime.now().time()),)
    try:

        EMAIL_SUBJECT = 'TEST EMAIL'
        EMAIL_MESSAGE = u'Привіт усім, це перевірка роботи щомісячного звіту.'
        EMAIL_EMAIL_FROM = 'eq@eq.com'
        EMAIL_EMAIL_TO = 'tarasinf2013@gmail.com'

        from django.core.mail import send_mail
        send_mail(EMAIL_SUBJECT, EMAIL_MESSAGE, EMAIL_EMAIL_FROM, [EMAIL_EMAIL_TO], fail_silently=False)
    except Exception, e:
        print '[send_email]', e


@task()
def send_email(lesson_id, user_id):
    print '[ SEND EMAIL ] [ %s ]' % (str(datetime.datetime.now().time()))

    try:
        lesson = Lesson.objects.get(id=lesson_id)
        user = User.objects.get(id=user_id)

        EMAIL_SUBJECT = 'Course: %s, Lesson[%s]: %s' % (lesson.course.name, str(lesson.number), lesson.name)
        EMAIL_MESSAGE = lesson.text
        EMAIL_EMAIL_FROM = 'eq@eq.com'
        EMAIL_EMAIL_TO = user.email

        from django.core.mail import send_mail
        send_mail(EMAIL_SUBJECT, EMAIL_MESSAGE, EMAIL_EMAIL_FROM, [EMAIL_EMAIL_TO], fail_silently=False)
    except Exception, e:
        print '[send_email]', e
