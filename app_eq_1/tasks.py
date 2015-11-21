#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from celery import task
from app_eq_1.models import UserCourse
from app_eq_1.models import Lesson
from app_eq_1.models import Action
import datetime


@task()
def example(t):
    print '[ EVERY_DAY ] [ %s ] %d' % (str(datetime.datetime.now().time()), t)

    try:
        for item in UserCourse.objects.filter(status='active').distinct():
            try:
                print "ITEM %s, type %s" % (item, type(item))
                if item.last_lesson < item.course.lesson_set.count():
                        action_new = Action(user_course=item, lesson=item.course.lesson_set.get(number=item.last_lesson + 1))
                        action_new.save()

                        item.last_lesson += 1
                        item.save()
                        send_email(1, 14)
                else:
                    item.status = 'ended'
                    item.save()
            except Exception, e:
                print e
    except Exception, e:
        print e


@task()
def every_day(t):
    print '[ EVERY_DAY ] [ %s ]' % (str(datetime.datetime.now().time()), t)
    send_email(1, 14)


@task()
def send_email(email_id, user_id):
    print '[ SEND EMAIL ] [ %s ]' % (str(datetime.datetime.now().time()))
    # from django.core.mail import send_mail

    # send_mail('Subject here', 'Here is the message.', 'from@example.com', ['tarasinf2013@gmail.com'], fail_silently=False)


