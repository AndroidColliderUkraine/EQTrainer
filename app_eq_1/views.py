from django.shortcuts 			import render
from .models 					import Course
from .models 					import Article
from .models 					import UserCourse
from django.http import JsonResponse

def home(request):
	# locale_init(request)
	# title_user = "%s" %(request.user) 
	# user_type = request.user.profile.type_user
	# text = _("Main page  :)")
	text = "Main page  :)"


	course_list = None
	try:
		course_list = Course.objects.filter(state='active').order_by('-updated')[:3]
	except Exception, e:
		print "e:", e
	# print "course_list: ", course_list


	article_list = None
	try:
		article_list = Article.objects.filter(state='active').order_by('-updated')[:3]
	except Exception, e:
		print "e:", e
	# print "article_list: ", article_list


	context = {
		# "title_user": title_user,
		"text": text,
		"course_list": course_list,
		"article_list": article_list,
	}
	return render(request, "index.html",context)


def profile(request):
	text = "Main page  :)"
	context = {
		"text": text,
	}
	return render(request, "profile.html",context)


def course(request):
	course_id = request.GET.get('id')
	if course_id != None:
		course = None
		try:
			course = Course.objects.filter(id=course_id).get()
		except Exception, e:
			print "e:", e
		
		try:
			subscribe = UserCourse.objects.filter(course=course).filter(user=request.user).exclude(status='ended').exists()
		except Exception, e:
			print 'e', e
			subscribe = False
		print 'subscribe', subscribe
		context = {
			"course": course,
			"subscribe": subscribe,
		}
		return render(request, "course.html",context)	
	else:
		course_list = None
		try:
			course_list = Course.objects.filter(state='active').order_by('-updated')[:3]
		except Exception, e:
			print "e:", e
		# print "course_list: ", course_list

		context = {
			"course_list": course_list,
		}
		return render(request, "courses.html",context)	


def article(request):
	article_id = request.GET.get('id')
	if article_id != None:
		article = None
		try:
			article = Article.objects.filter(id=article_id).get()
		except Exception, e:
			print "e:", e
		context = {
			"article": article,
		}
		return render(request, "article.html",context)	
	else:
		article_list = None
		try:
			article_list = Article.objects.filter(state='active').order_by('-updated')[:3]
		except Exception, e:
			print "e:", e
		# print "article_list: ", article_list

		context = {
			"article_list": article_list,
		}
		return render(request, "articles.html",context)	


def subscribe_course(request):
	course_id = request.GET.get('id')

	if course_id != None and request.user.is_authenticated():
		return JsonResponse({'State':str(Course.subscribe(course_id, request.user)) })
	else:
		return JsonResponse({'State':'ERROR: id == None or user is not authenticated'})	


def unsubscribe_course(request):
	course_id = request.GET.get('id')

	if course_id != None and request.user.is_authenticated():
		return JsonResponse({'State':str(Course.unsubscribe(course_id, request.user)) })
	else:
		return JsonResponse({'State':'ERROR: id == None or user is not authenticated'})	

