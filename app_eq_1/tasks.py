#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from celery import task
from app_eq_1.models import UserCourse
from app_eq_1.models import Lesson
from app_eq_1.models import Action
from app_eq_1.models import Conclusions
from app_eq_1.models import WeeklyReport, MonthlyReport
from django.contrib.auth.models import User
from datetime import timedelta, datetime
from django.utils import timezone
from app_eq_1.constants import USER_EMOTIONS, USER_ACTIVITY
from django.shortcuts 			import render
from django.template import loader, Context
from django.template.loader import render_to_string
from django.db.models import Sum


@task()
def example():
    print '[ EVERY_30_SECONDS ] [ %s ]' % (str(datetime.now().time()),)
    every_week()


@task()
def every_day():
    print '[ EVERY_DAY ] [ %s ]' % (str(datetime.now().time()),)

    try:
        for item in UserCourse.objects.filter(deleted=False).filter(status='active').distinct():
            try:
                if item.last_lesson < item.course.lesson_set.count():
                    action_new = Action(user_course=item,
                                        lesson=item.course.lesson_set.get(number=item.last_lesson + 1))
                    action_new.save()

                    item.last_lesson += 1
                    item.save()
                    send_email_lesson(item.course.lesson_set.get(number=item.last_lesson).id, item.user.id)
                else:
                    item.status = 'ended'
                    item.save()
            except Exception, e:
                print e
    except Exception, e:
        print e


@task()
def every_week():
    print '[ EVERY_WEEK ] [ %s ]' % (str(datetime.now().time()),)
    try:
        some_day_last_week = datetime.now().date() - timedelta(days=7)
        monday_of_last_week = some_day_last_week - timedelta(days=(some_day_last_week.isocalendar()[2] - 1))
        monday_of_this_week = monday_of_last_week + timedelta(days=7)

        for user in User.objects.all():
            try:
                ratings = {}
                for emotion in USER_EMOTIONS:
                    temp = {}
                    for activity in USER_ACTIVITY:
                        temp[activity[0]] = 0
                    ratings[emotion[0]] = temp

                emotional_states = user.emotionalstate_set.filter(
                    updated__gte=monday_of_last_week,
                    updated__lt=monday_of_this_week)
                if not emotional_states:
                    continue
                for emotional_state in emotional_states:
                    ratings[emotional_state.emotion][emotional_state.activity] += emotional_state.subjectivity * emotional_state.confidence

                winner = 0
                winner_activity = None
                winner_emotion = None
                for emotion in ratings:
                    for activity in ratings[emotion]:
                        if ratings[emotion][activity] > winner:
                            winner = ratings[emotion][activity]
                            winner_activity = activity
                            winner_emotion = emotion

                if winner:
                    conclusion = Conclusions.objects.\
                        filter(activity__exact=winner_activity).\
                        filter(emotion__exact=winner_emotion)[0]
                    # create report
                    context = {
                        "user": user,
                        "text": conclusion.text,
                    }
                    context.update(
                        get_context_for_reports(
                            user_id=user.id,
                            date_start=monday_of_last_week,
                            date_end=monday_of_this_week
                        )
                    )

                    report = WeeklyReport.objects.create(
                        user=user,
                        text=render_to_string('email/week_report.html', context)
                    )

                    # send email
                    send_email_report_week(
                        week_report_id=report.id,
                        user_id=user.id
                    )
            except Exception, e:
                print e
    except Exception, e:
        print e


@task
def every_month():
    print '[ EVERY_MONTH ] [ %s ]' % (str(datetime.now().time()),)
    try:
        some_day_last_month = datetime.now().date() - timedelta(days=28)
        monday_of_last_month = some_day_last_month - timedelta(days=(some_day_last_month.isocalendar()[2] - 1))
        monday_of_this_month = monday_of_last_month + timedelta(days=28)
        for user in User.objects.all():
            try:
                ratings = {}
                for emotion in USER_EMOTIONS:
                    temp = {}
                    for activity in USER_ACTIVITY:
                        temp[activity[0]] = 0
                    ratings[emotion[0]] = temp
                emotional_states = user.emotionalstate_set.filter(
                    updated__gte=monday_of_last_month,
                    updated__lt=monday_of_this_month)
                if not emotional_states:
                    continue
                for emotional_state in emotional_states:
                    ratings[emotional_state.emotion][emotional_state.activity] += emotional_state.subjectivity * emotional_state.confidence
                winner = 0
                winner_activity = None
                winner_emotion = None
                for emotion in ratings:
                    for activity in ratings[emotion]:
                        if ratings[emotion][activity] > winner:
                            winner = ratings[emotion][activity]
                            winner_activity = activity
                            winner_emotion = emotion

                if winner:
                    print 'Winner:', winner_activity, winner_emotion, winner
                    conclusion = Conclusions.objects.\
                        filter(activity__exact=winner_activity).\
                        filter(emotion__exact=winner_emotion)[0]
                    # create report
                    context = {
                        "user": user,
                        "text": conclusion.text,
                    }

                    report = MonthlyReport.objects.create(
                        user=user,
                        text=render_to_string('email/month_report.html', context)
                    )
                    # send email
                    send_email_report_month(
                        month_report_id=report.id,
                        user_id=user.id
                    )
            except Exception, e:
                print e
    except Exception, e:
        print e


@task()
def send_email_lesson(lesson_id, user_id):
    print '[ SEND EMAIL ] [ %s ]' % (str(datetime.now().time()))

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
        print '[send_email_lesson]', e


@task()
def send_email_report_week(week_report_id, user_id):
    print '[ SEND EMAIL WEEKLY REPORT ] [ %s ]' % (str(datetime.now().time()))

    try:
        report = WeeklyReport.objects.get(id=week_report_id)
        user = User.objects.get(id=user_id)
        EMAIL_SUBJECT = 'Week report [%s - %s]' % (str(report.updated), str(report.updated - timedelta(days=7)))
        EMAIL_MESSAGE = report.text
        EMAIL_EMAIL_FROM = 'eq@eq.com'
        EMAIL_EMAIL_TO = user.email

        from django.core.mail import send_mail
        send_mail(
            subject=EMAIL_SUBJECT,
            message="It's doesn't matter, how we have 'html_message'.",
            from_email=EMAIL_EMAIL_FROM,
            recipient_list=[EMAIL_EMAIL_TO],
            fail_silently=False,
            html_message=EMAIL_MESSAGE)
    except Exception, e:
        print '[send_email_weekly_report]', e


@task()
def send_email_report_month(month_report_id, user_id):
    print '[ SEND EMAIL WEEKLY REPORT ] [ %s ]' % (str(datetime.now().time()))

    try:
        report = MonthlyReport.objects.get(id=month_report_id)
        user = User.objects.get(id=user_id)
        EMAIL_SUBJECT = 'Month report [%s - %s]' % (str(report.updated), str(report.updated - timedelta(days=28)))
        EMAIL_MESSAGE = report.text
        EMAIL_EMAIL_FROM = 'eq@eq.com'
        EMAIL_EMAIL_TO = user.email

        from django.core.mail import send_mail
        send_mail(
            subject=EMAIL_SUBJECT,
            message="It's doesn't matter, how we have 'html_message'.",
            from_email=EMAIL_EMAIL_FROM,
            recipient_list=[EMAIL_EMAIL_TO],
            fail_silently=False,
            html_message=EMAIL_MESSAGE)
    except Exception, e:
        print '[send_email_weekly_report]', e


def get_context_for_reports(user_id, date_start, date_end):
    print "I'm in get_context_for_reports"

    confidence_reports = 0
    confidence_reports_total = 0
    subjectivity_reports = 0
    subjectivity_reports_total = 0
    emotion_activity = []

    try:
        user = User.objects.get(id=user_id)

        confidence_reports = user.emotionalstate_set.\
            filter(deleted=False).\
            filter(updated__gte=date_start).\
            filter(updated__lt=date_end).\
            aggregate(Sum('confidence'))['confidence__sum']
        confidence_reports_total = user.emotionalstate_set.\
            filter(deleted=False).\
            filter(updated__gte=date_start).\
            filter(updated__lt=date_end).\
            count() * 100
        confidence_reports_total = 100 if confidence_reports_total == 0 else confidence_reports_total
        confidence_reports = 0 if confidence_reports is None else confidence_reports

        subjectivity_reports = user.emotionalstate_set.\
            filter(deleted=False).\
            filter(updated__gte=date_start).\
            filter(updated__lt=date_end).\
            aggregate(Sum('subjectivity'))['subjectivity__sum']
        subjectivity_reports_total = user.emotionalstate_set.\
            filter(deleted=False).\
            filter(updated__gte=date_start).\
            filter(updated__lt=date_end).\
            count() * 100
        subjectivity_reports_total = 100 if subjectivity_reports_total == 0 else subjectivity_reports_total
        subjectivity_reports = 0 if subjectivity_reports is None else subjectivity_reports

        print 'Test_ print'
        # print 'USER_EMOTIONS', USER_EMOTIONS
        for emotion, name_e in USER_EMOTIONS:
            # print '---', emotion, name_e
            temp = []
            sum = 0
            for activity, name_a in USER_ACTIVITY:
                a = user.emotionalstate_set.\
                    filter(deleted=False).\
                    filter(updated__gte=date_start).\
                    filter(updated__lt=date_end).\
                    filter(emotion=emotion).\
                    filter(activity=activity).\
                    count()
                # print 'EM:', name_a,
                sum += int(a)
                temp.append(a)
            temp.append(sum)
            emotion_activity.append([name_e, temp])

        # for a, b in emotion_activity:
        #     print 'AAA', a, '|||', b

    except Exception, e:
        print "e:", e

    context = {
        "confidence_reports": confidence_reports,
        "confidence_reports_total": confidence_reports_total,
        "subjectivity_reports": subjectivity_reports,
        "subjectivity_reports_total": subjectivity_reports_total,
        "user_emotions": USER_EMOTIONS,
        "user_activity": USER_ACTIVITY,
        "emotion_activity": emotion_activity,
    }
    return context
