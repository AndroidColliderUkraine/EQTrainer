# -*- coding: utf-8 -*-
from django.db 						import models
from django.contrib.auth.models 	import User
from constants 						import *


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
	def __unicode__(self):
		return self.name


class Lesson(models.Model):
	name = models.CharField(max_length=500, blank=True, null=True)
	tags = models.CharField(max_length=5000, blank=True, null=True)
	text = models.TextField(max_length=120, blank=True, null=True)
	course = models.ForeignKey(Course, blank=False, null=False)
	number = models.IntegerField(unique=True)
	state = models.CharField(choices=STATE, max_length=20, blank=False, null=True, default='not_active') 
	
	# date = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	def __unicode__(self):
		return (str(self.number) + ' | ' + str(self.name))


class Article(models.Model):
	name = models.CharField(max_length=500, blank=True, null=True)
	tags = models.CharField(max_length=500, blank=True, null=True)
	headline = models.TextField(max_length=120, blank=True, null=True)
	text = models.TextField(max_length=5000, blank=True, null=True)
	photo = models.URLField(blank=True, null=True, verbose_name=('Photo'))
	state = models.CharField(choices=STATE, max_length=20, blank=False, null=True, default='not_active') 
	
	# date = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	def __unicode__(self):
		return self.name


class UserCourse(models.Model):
	user = models.ForeignKey(User, blank=False, null=False)
	course = models.ForeignKey(Course, blank=False, null=False)

	# state = models.CharField(choices=STATE, max_length=20, blank=False, null=True, default='not_active') 
	paid = models.BooleanField(default=True)

	# date = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	def __unicode__(self):
		return self.id

class Action(models.Model):
	user_course = models.ForeignKey(UserCourse, blank=False, null=False)
	lesson = models.ForeignKey(Lesson, blank=False, null=False)

	# date = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	def __unicode__(self):
		return self.id


class EmotionalState(models.Model):
	fear = models.IntegerField(default=20)# max=100, min=0
	confidence = models.IntegerField(default=20)# max=100, min=0
	#
	#
	user = models.ForeignKey(User, blank=False, null=False)
	subjectivity = models.IntegerField(default=20)# max=100, min=0

	# date = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)	
	def __unicode__(self):
		return (str(self.user) + '|' + str(self.date))

