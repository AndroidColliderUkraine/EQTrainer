# -*- coding: utf-8 -*-
from django.db 						import models
from django.contrib.auth.models 	import User
from constants 						import *
from redactor.fields                import RedactorField
import os
from django.conf import settings


class UserProfile(models.Model):
    # user = models.OneToOneField(User, related_name='profile', default='avatars/default.png')
    user = models.OneToOneField(User, related_name='profile')
    avatar = models.ImageField(upload_to='avatars', default=None, blank=True, null=True)


class Course(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    tags = models.CharField(max_length=500, blank=True, null=True)
    text = models.TextField(max_length=5000, blank=True, null=True)
    photo = models.URLField(blank=True, null=True)
    small_photo = models.URLField(blank=True, null=True)
    icon = models.URLField(blank=True, null=True)
    state = models.CharField(choices=STATE, max_length=20, blank=False, null=True, default='not_active')
    price = models.IntegerField(default=0)
    video = models.URLField(blank=True, null=True)

    # date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.name)

    @staticmethod
    def subscribe(course_id, user_id):
        print "I'm in subscribe"
        try:
            course = Course.objects.get(id=course_id)
            user = User.objects.get(id=user_id)
            if not UserCourse.objects.filter(deleted=False).filter(course=course).filter(user=user).exclude(status='ended').exists():
                if course.price == 0:
                    usercourse_new = UserCourse(course=course, user=user, status='active')
                else:
                    usercourse_new = UserCourse(course=course, user=user, status='begin')
                usercourse_new.save()
                return True
        except Exception, e:
            print e

        return False

    @staticmethod
    def unsubscribe(course_id, user_id):
        print "I'm in unsubscribe"
        try:
            course = Course.objects.get(id=course_id)
            user = User.objects.get(id=user_id)
            user_courses = UserCourse.objects.\
                filter(deleted=False)\
                .filter(course=course)\
                .filter(user=user)\
                .exclude(status='ended')[:1]

            for item in user_courses:
                item.deleted = True
                item.save()
            return True
        except Exception, e:
            print e
            return False


class Lesson(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    tags = models.CharField(max_length=5000, blank=True, null=True)
    text = models.TextField(max_length=120, blank=True, null=True)
    course = models.ForeignKey(Course, blank=False, null=False)
    number = models.IntegerField()
    state = models.CharField(choices=STATE, max_length=20, blank=False, null=True, default='not_active')

    # date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.number) + ' | ' + str(self.name)

    class Meta:
        unique_together = ('number', 'course',)


class Article(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    tags = models.CharField(max_length=500, blank=True, null=True)
    headline = models.TextField(max_length=120, blank=True, null=True)
    # text = models.TextField(max_length=5000, blank=True, null=True)
    text = RedactorField(verbose_name=u'Text')

    photo = models.URLField(blank=True, null=True, verbose_name=('Photo'))
    state = models.CharField(choices=STATE, max_length=20, blank=False, null=True, default='not_active')

    # date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class UserCourse(models.Model):
    user = models.ForeignKey(User, blank=False, null=False)
    course = models.ForeignKey(Course, blank=False, null=False)

    status = models.CharField(choices=USER_COURSE_STATUS, max_length=20, blank=False, null=True, default='begin')
    # paid = models.BooleanField(default=True)
    last_lesson = models.IntegerField(default=0)
    # date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.id)


class Action(models.Model):
    user_course = models.ForeignKey(UserCourse, blank=False, null=False)
    lesson = models.ForeignKey(Lesson, blank=False, null=False)

    # date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.id)


class EmotionalState(models.Model):
    emotion = models.CharField(choices=USER_EMOTIONS, max_length=50, blank=False, null=True)
    activity = models.CharField(choices=USER_ACTIVITY, max_length=50, blank=False, null=True)

    user = models.ForeignKey(User, blank=False, null=False)
    subjectivity = models.IntegerField(default=20)  # max=100, min=0
    confidence = models.IntegerField(default=20)  # max=100, min=0

    # date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.id)


class WeeklyReport(models.Model):
    user = models.ForeignKey(User, blank=False, null=False)
    text = models.TextField(max_length=5000, blank=False, null=True)
    html = models.TextField(max_length=5000, blank=False, null=True, help_text='Use in Email for Reports.')
    date_start = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)

    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(unicode(self.user) + ' | ' + unicode(self.updated))


class MonthlyReport(models.Model):
    user = models.ForeignKey(User, blank=False, null=False)
    text = models.TextField(max_length=5000, blank=False, null=True)
    html = models.TextField(max_length=5000, blank=False, null=True, help_text='Use in Email for Reports.')
    date_start = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)

    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(unicode(self.user) + ' | ' + unicode(self.updated))


class Training(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)
    text = models.TextField(max_length=5000, blank=False, null=True)

    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.name)


class Conclusions(models.Model):
    class Meta:
        unique_together = ('emotion', 'activity')
    emotion = models.CharField(choices=USER_EMOTIONS, max_length=50, blank=False, null=True)
    activity = models.CharField(choices=USER_ACTIVITY, max_length=50, blank=False, null=True)
    text = models.TextField(max_length=5000)

    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.id)