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
                        send_email(item.course.lesson_set.get(number=item.last_lesson).id, item.user.id)
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
def send_email(lesson_id, user_id):
    print '[ SEND EMAIL ] [ %s ]' % (str(datetime.datetime.now().time()))
    print "lesson _id", lesson_id
    print 'user_id', user_id
    try:
        lesson = Lesson.objects.get(id=lesson_id)
        print 'lesson', lesson

        user = User.objects.get(id=user_id)
        print 'user', user
        print 'p_1'
        EMAIL_SUBJECT = 'Course: %s, Lesson[%s]: %s' % (lesson.course.name, str(lesson.number), lesson.name)
        EMAIL_MESSAGE = lesson.text
        EMAIL_EMAIL_FROM = 'eq@eq.com'
        EMAIL_EMAIL_TO = user.email
        print 'p_2'
        from django.core.mail import send_mail
        print 'p_3'
        send_mail(EMAIL_SUBJECT, EMAIL_MESSAGE, EMAIL_EMAIL_FROM, [EMAIL_EMAIL_TO], fail_silently=False)
        print 'p_4'
    except Exception, e:
        print e


