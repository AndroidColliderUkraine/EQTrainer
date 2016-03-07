from django.shortcuts 			import render
from .models 					import Course
from .models 					import Article
from .models 					import UserCourse
from .models 					import Action
from .models 					import Lesson
from .models import WeeklyReport
from .models import MonthlyReport
from .models import Training
from django.contrib.auth.models 	import User
from django.http import JsonResponse
import datetime
import pytz
from django.db.models import Sum
from constants import USER_EMOTIONS, USER_ACTIVITY, TIME_FORMAT


def home(request):
    if request.user.is_authenticated():
        # return home_private(request)
        return profile_mydaybook(request)
    else:
        return home_public(request)


def home_public(request):
    course_list = None
    try:
        course_list = Course.objects.filter(deleted=False).filter(state='active').order_by('-updated')[:3]
    except Exception, e:
        print "e:", e
    # print "course_list: ", course_list

    article_list = None
    try:
        article_list = Article.objects.filter(deleted=False).filter(state='active').order_by('-updated')[:3]
    except Exception, e:
        print "e:", e
    # print "article_list: ", article_list

    context = {
        "course_list": course_list,
        "article_list": article_list,
    }
    return render(request, "index.html", context)


def home_private(request):
    text = "Main page  :)"
    context = {
        "text": text,
    }
    return render(request, "profile.html", context)


def courses(request):
    if request.user.is_authenticated():
        return courses_private(request)
    else:
        return courses_public(request)


def courses_public(request):
    course_list = None
    try:
        course_list = Course.objects.filter(deleted=False).filter(state='active').order_by('-updated')[:3]
    except Exception, e:
        print "e:", e

    context = {
        "course_list": course_list,
    }
    return render(request, "courses.html", context)


def courses_private(request):
    print "I'm in profile_courses"
    course_list = None
    try:
        course_list = Course.objects.filter(deleted=False).filter(state='active').order_by('-updated')[:3]
    except Exception, e:
        print "e:", e
    # print "course_list: ", course_list

    context = {
        "course_list": course_list,
    }
    return render(request, "profile_courses.html", context)


def course(request):
    if request.user.is_authenticated():
        return course_private(request)
    else:
        return course_public(request)


def course_public(request):
    course_id = request.GET.get('id')
    course = None
    try:
        course = Course.objects.filter(deleted=False).filter(id=course_id).get()
    except Exception, e:
        print "e:", e

    try:
        subscribe = UserCourse.objects.filter(deleted=False).filter(course=course).filter(user=request.user).exclude(status='ended').exists()
    except Exception, e:
        print 'e', e
        subscribe = False
    print 'subscribe', subscribe
    context = {
        "course": course,
        "subscribe": subscribe,
    }
    return render(request, "course.html", context)


def course_private(request):
    print "I'm in profile_course"
    course_id = request.GET.get('id')
    course = None
    try:
        course = Course.objects.filter(deleted=False).filter(id=course_id).get()
    except Exception, e:
        print "e:", e

    try:
        subscribe = UserCourse.objects.filter(deleted=False).filter(course=course).filter(user=request.user).exclude(status='ended').exists()
    except Exception, e:
        print 'e', e
        subscribe = False
    print 'subscribe', subscribe
    context = {
        "course": course,
        "subscribe": subscribe,
    }
    return render(request, "profile_course.html", context)


def articles(request):
    if request.user.is_authenticated():
        return articles_private(request)
    else:
        return articles_public(request)


def articles_public(request):
    article_list = None
    try:
        article_list = Article.objects.filter(deleted=False).filter(state='active').order_by('-updated')[:3]
    except Exception, e:
        print "e:", e
    # print "article_list: ", article_list

    context = {
        "article_list": article_list,
    }
    return render(request, "articles.html", context)


def articles_private(request):
    print "I'm in profile_articles"
    article_list = None
    try:
        article_list = Article.objects.filter(deleted=False).filter(state='active').order_by('-updated')[:3]
    except Exception, e:
        print "e:", e
    # print "article_list: ", article_list

    context = {
        "article_list": article_list,
    }
    return render(request, "profile_articles.html", context)


def article(request):
    if request.user.is_authenticated():
        return article_private(request)
    else:
        return article_public(request)


def article_private(request):
    article_id = request.GET.get('id')
    article = None
    try:
        article = Article.objects.filter(deleted=False).filter(id=article_id).get()
    except Exception, e:
        print "e:", e
    context = {
        "article": article,
    }
    return render(request, "profile_arcticle.html", context)


def article_public(request):
    article_id = request.GET.get('id')
    article = None
    try:
        article = Article.objects.filter(deleted=False).filter(id=article_id).get()
    except Exception, e:
        print "e:", e
    context = {
        "article": article,
    }
    return render(request, "article.html", context)


def subscribe_course(request):
    course_id = request.GET.get('course_id')
    user_id = request.GET.get('user_id')
    if course_id != None and user_id != None:
        return JsonResponse({'State': str(Course.subscribe(course_id, user_id))})
    else:
        return JsonResponse({'State': 'ERROR: id == None or user is not authenticated'})


def unsubscribe_course(request):
    course_id = request.GET.get('course_id')
    user_id = request.GET.get('user_id')
    if course_id != None and user_id != None:
        return JsonResponse({'State': str(Course.unsubscribe(course_id, user_id))})
    else:
        return JsonResponse({'State': 'ERROR: id == None or user is not authenticated'})


def profile_mycourses(request):
    print "I'm in profile_mycourses"
    if request.user.is_authenticated():
        usercourses_ended = None
        usercourses_not_ended = None
        try:
            usercourses_ended = UserCourse.objects.filter(deleted=False).filter(user=request.user).filter(status='ended').order_by('-updated')
            usercourses_not_ended = UserCourse.objects.filter(deleted=False).filter(user=request.user).exclude(status='ended').order_by('-updated')
        except Exception, e:
            print "e:", e

    context = {
        'usercourses_ended': usercourses_ended,
        'usercourses_not_ended': usercourses_not_ended,
    }
    return render(request, "profile_mycourses.html", context)


def profile_myusercourse(request):
    print "I'm in profile_myusercourse"
    user_course_id = request.GET.get('id')
    print "id", user_course_id
    user_course = None
    lessons = None
    try:
        user_course = UserCourse.objects.filter(deleted=False).get(id=user_course_id)
        # lessons = user_course.course.lesson_set.all()
        actions = user_course.action_set.filter(deleted=False).all()
        lessons = set()
        for action in actions:
            lessons.add(action.lesson)
        # lessons = user_course.action_set.select_related('lesson')
        print 'lessons', lessons
    except Exception, e:
        print "e:", e

    context = {
        "user_course": user_course,
        "lessons": lessons,
    }
    return render(request, "profile_mycourse.html", context)


# def profile_mylesson(request):
#     print "I'm in profile_mylesson"
#     lesson_id = request.GET.get('id')
#     lesson = None
#
#     try:
#         lesson = Course.objects.filter(id=lesson_id).get()
#     except Exception, e:
#         print "e:", e
#
#     context = {
#         "lesson": lesson,
#     }
#     return render(request, "profile_mylesson.html", context)


def profile_mydaybook(request):
    print "I'm in profile_mydaybook"
    # user_id = request.GET.get('user_id')
    weekly_reports = None
    monthly_reports = None

    confidence_reports = 0
    confidence_reports_total = 0
    subjectivity_reports = 0
    subjectivity_reports_total = 0
    emotion_activity = []

    try:
        weekly_reports = request.user.weeklyreport_set.filter(deleted=False).order_by('-updated').all()[:10]
        monthly_reports = request.user.monthlyreport_set.filter(deleted=False).order_by('-updated').all()[:5]

        preview_week = datetime.datetime.now() - datetime.timedelta(weeks=3)

        confidence_reports = request.user.emotionalstate_set.\
            filter(deleted=False).\
            filter(updated__gte=preview_week).\
            aggregate(Sum('confidence'))['confidence__sum']
        confidence_reports_total = request.user.emotionalstate_set.\
            filter(deleted=False).\
            filter(updated__gte=preview_week).\
            count() * 100
        confidence_reports_total = 100 if confidence_reports_total == 0 else confidence_reports_total
        confidence_reports = 0 if confidence_reports is None else confidence_reports

        subjectivity_reports = request.user.emotionalstate_set.\
            filter(deleted=False).\
            filter(updated__gte=preview_week).\
            aggregate(Sum('subjectivity'))['subjectivity__sum']
        subjectivity_reports_total = request.user.emotionalstate_set.\
            filter(deleted=False).\
            filter(updated__gte=preview_week).\
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
                a = request.user.emotionalstate_set.\
                    filter(deleted=False).\
                    filter(updated__gte=preview_week).\
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
        "weekly_reports": weekly_reports,
        "monthly_reports": monthly_reports,
        "confidence_reports": confidence_reports,
        "confidence_reports_total": confidence_reports_total,
        "subjectivity_reports": subjectivity_reports,
        "subjectivity_reports_total": subjectivity_reports_total,
        "user_emotions": USER_EMOTIONS,
        "user_activity": USER_ACTIVITY,
        "emotion_activity": emotion_activity,
    }
    return render(request, "profile_mydaybook.html", context)


def trener(request):
    if request.user.is_authenticated():
        return trener_private(request)
    else:
        return trener_public(request)


def trener_private(request):
    try:
        trainings = Training.objects.filter(deleted=False).all()
    except Exception, e:
        print "e:", e
        trainings = None

    context = {
        "trainings": trainings,
    }

    return render(request, "profile_trener.html", context)


def trener_public(request):
    try:
        trainings = Training.objects.filter(deleted=False).all()
    except Exception, e:
        print "e:", e
        trainings = None

    context = {
        "trainings": trainings,
    }

    return render(request, "trener.html", context)


def about(request):
    if request.user.is_authenticated():
        return about_private(request)
    else:
        return about_public(request)


def about_private(request):
    return render(request, "profile_about.html", {})


def about_public(request):
    return render(request, "about.html", {})


def report_graph(request):
    try:
        from .tasks import get_context_for_reports
        date_start = request.GET['date_start']
        date_end = request.GET['date_end']
        user_id = request.GET['user_id']
        print 'date_start', date_start
        print 'date_end', date_end
        print 'user_id', user_id

        date_start = datetime.datetime.strptime(date_start, TIME_FORMAT).replace(tzinfo=pytz.utc)
        date_end = datetime.datetime.strptime(date_end, TIME_FORMAT).replace(tzinfo=pytz.utc)
        user_id = int(user_id)

        context = get_context_for_reports(
            user_id=user_id,
            date_start=date_start,
            date_end=date_end
        )

        return render(request, "email/week_report_graph.html", context=context)
    except Exception, e:
        print "e:", e


def lawyer_page(request):
    context = {}
    return render(request, "lawyer_page.html", context=context)
