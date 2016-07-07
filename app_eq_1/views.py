# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts 			import render
from .models 					import Course
from .models 					import Article
from .models 					import UserCourse
from .models 					import UserProfile
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
from constants import USER_EMOTIONS, USER_ACTIVITY, TIME_FORMAT, COURSE_PER_PAGE
import logging
logger = logging.getLogger(__name__)


def home_old(request):
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
    return render(request, "index_old.html", context)


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
    from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
    try:
        course_list = Course.objects.filter(deleted=False).filter(state='active').order_by('-created')
        paginator = Paginator(course_list, COURSE_PER_PAGE)
        page = request.GET.get('page')
        try:
            courses = paginator.page(page)
        except PageNotAnInteger:
            print 'OOOOOOOOOOOOo 1'
            courses = paginator.page(1)
        except EmptyPage:
            print 'OOOOOOOOOOOOo 2'
            courses = paginator.page(paginator.num_pages)
    except Exception, e:
        print "e:", e

    # print "article_list: ", article_list
    print 'ARTICLES', courses
    context = {
        "course_list": courses,
    }
    return render(request, "courses.html", context)


def courses_private(request):
    print "I'm in profile_courses"
    from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
    try:
        course_list = Course.objects.filter(deleted=False).filter(state='active').order_by('-created')
        paginator = Paginator(course_list, COURSE_PER_PAGE)
        page = request.GET.get('page')
        try:
            courses = paginator.page(page)
        except PageNotAnInteger:
            courses = paginator.page(1)
        except EmptyPage:
            courses = paginator.page(paginator.num_pages)
    except Exception, e:
        print "e:", e

    # print "article_list: ", article_list
    print 'ARTICLES', courses
    context = {
        "course_list": courses,
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
    from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
    try:
        article_list = Article.objects.filter(deleted=False).filter(state='active').order_by('-updated')
        paginator = Paginator(article_list, 2)
        page = request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            print 'OOOOOOOOOOOOo 1'
            articles = paginator.page(1)
        except EmptyPage:
            print 'OOOOOOOOOOOOo 2'
            articles = paginator.page(paginator.num_pages)
    except Exception, e:
        print "e:", e

    # print "article_list: ", article_list
    print 'ARTICLES', articles
    context = {
        "article_list": articles,
    }
    return render(request, "articles.html", context)


def articles_private(request):
    from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
    print "I'm in profile_articles"
    try:
        article_list = Article.objects.filter(deleted=False).filter(state='active').order_by('-updated')
        paginator = Paginator(article_list, 2)
        page = request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            print 'OOOOOOOOOOOOo 1'
            articles = paginator.page(1)
        except EmptyPage:
            print 'OOOOOOOOOOOOo 2'
            articles = paginator.page(paginator.num_pages)

    except Exception, e:
        print "e:", e

    # print "article_list: ", article_list
    print 'ARTICLES', articles
    context = {
        "article_list": articles,
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
    from datetime import timedelta
    some_day_this_week = datetime.datetime.now().date()

    date_start = some_day_this_week - timedelta(days=(some_day_this_week.isocalendar()[2] - 1))
    date_end = date_start + timedelta(days=7)
    user_id = int(request.user.id)

    context = get_context_for_reports(
        user_id=user_id,
        date_start=date_start,
        date_end=date_end
    )

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


def term_of_use(request):
    context = {}
    return render(request, "term_of_use.html", context=context)


def profile_my_conclusions(request):
    print "I'm my_conclusion"
    context = {
        "trainings": '',
    }

    return render(request, "profile_myconclusions.html", context)


def profile_my_setting(request):
    from .forms import UserForm, UserProfileForm
    from .models import UserProfile
    if request.method == "POST":
        uform = UserForm(data=request.POST, instance=request.user)
        pform = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user.profile)
        if uform.is_valid():
            print '|||||||||||', 'uForm valid'
            uform.save()
        else:
            print '|||||||||||', 'uForm invalid', uform.errors
        if pform.is_valid():
            print '|||||||||||', 'pForm valid'
            pform.save()
        else:
            print '|||||||||||', 'pForm invalid', pform.errors
    print "I'm my_conclusion"
    uform = UserForm(instance=request.user)

    # userProfile, created = UserProfile.objects.get_or_create(user=request.user, avatar=None)
    pform = UserProfileForm(instance=request.user.profile)
    context = {
        'domain': request.META['HTTP_HOST'],
        'uid': urlsafe_base64_encode(force_bytes(request.user.pk)),
        'token': default_token_generator.make_token(request.user),
        "trainings": '',
        "uform": uform,
        "pform": pform,
    }

    return render(request, "profile_mysettings.html", context)


def unsubscribe_mailing(request):
    try:
        up, created = UserProfile.objects.get_or_create(user_id=request.GET.get('user_id'))
        up.subscribe_mailing = False
        up.save()
        context = {
            'user': up.user
        }
        return render(request, "email/unsubscribe_mailing.html", context)
    except Exception, e:
        print "e:", e
    return render(request, "email/unsubscribe_mailing.html", {})


def custom_login(request):
    context = {'error': 'None'}
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
            else:
                context['error'] = 'Non active user'
        else:
            context['error'] = u'Неправильная почта или пароль'
    except:
        context['error'] = ''

    return JsonResponse(context)


def custom_register(request):
    context = {'error': 'None'}
    if request.method == 'POST':
        # from django.contrib.auth.forms import UserCreationForm
        from app_eq_1.forms import UserRegistrationForm
        uform = UserRegistrationForm(data=request.POST)

        if uform.is_valid():
            user = uform.save()
            user_for_login = authenticate(username=user.username, password=uform.cleaned_data['password1'])
            if user_for_login is not None:
                if user_for_login.is_active:
                    auth_login(request, user_for_login)
        else:
            print uform.errors
            if u'A user with that username already exists.' in str(uform.errors):
                context['error'] = u'Пользователь с таким именем уже существует.'
            elif u'This field is required' in str(uform.errors):
                context['error'] = u'Заполните пустые поля.'
            elif u'Enter a valid email address' in str(uform.errors):
                context['error'] = u'Введите действительный адрес электронной почты.'
            else:
                # context['error'] = u'Некоторые ошибки происходит.'
                context['error'] = str(uform.errors)
    else:
        context['error'] = 'Not POST request.'

    return JsonResponse(context)


from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template import loader
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from tasks import send_email, get_context_for_reports
from django.views.generic import *
from forms import PasswordResetRequestForm, SetPasswordForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models.query_utils import Q


class ResetPasswordRequestView(FormView):
    # template_name = "account/test_template.html"    #code for template is given below the view's code
    success_url = '/account/login'
    form_class = PasswordResetRequestForm

    @staticmethod
    def validate_email_address(email):
        """
        This method here validates the if the input is an email address or not. Its return type is boolean, True if the input is a email address or False if its not.
        """
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    def post(self, request, *args, **kwargs):
        """
        A normal post request which takes input from field "email_or_username" (in ResetPasswordRequestForm).
        """
        context = {'error': 'None'}
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data["email_or_username"]
            if self.validate_email_address(data) is True:                 #uses the method written above
                '''
                If the input is an valid email address, then the following code will lookup for users associated with that email address. If found then an email will be sent to the address, else an error message will be printed on the screen.
                '''
                associated_users = User.objects.filter(Q(email=data) | Q(username=data))
                if associated_users.exists():
                    for user in associated_users:
                        c = {
                            'email': user.email,
                            'domain': request.META['HTTP_HOST'],
                            'site_name': 'EQ',
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'user': user,
                            'token': default_token_generator.make_token(user),
                            'protocol': 'http',
                            }
                        email_template_name ='account/password_reset_email.html'
                        email = loader.render_to_string(email_template_name, c)
                        send_email.delay(
                            EMAIL_SUBJECT=u'EQ: восстановление пароля',
                            EMAIL_EMAIL_FROM=u'Карманный Психолог <denyseq@ua.fm>',
                            EMAIL_EMAIL_TO=user.email,
                            EMAIL_MESSAGE=email
                        )
                    context['success'] = u'E-mail был отправлен ' + data + u". Пожалуйста, проверьте его почтовый ящик для продолжения сброса пароля."
                    return JsonResponse(context)
                context['error'] = u'Ни один пользователь не связан с этим адресом электронной почты'
                return JsonResponse(context)
        context['error'] = 'Invalid Input'
        return JsonResponse(context)


class PasswordResetConfirmView(FormView):
    template_name = "account/password_reset_confirm.html"
    success_url = '/'
    form_class = SetPasswordForm
    success_message = 'success_message'

    def post(self, request, uidb64=None, token=None, *arg, **kwargs):
        """
        View that checks the hash in a password reset link and presents a
        form for entering a new password.
        """
        form = self.form_class(request.POST)
        assert uidb64 is not None and token is not None  # checked by URLconf
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            if form.is_valid():
                new_password = form.cleaned_data['new_password2']
                user.set_password(new_password)
                user.save()
                messages.success(request, u'Пароль был сброшен.')
                return self.form_valid(form)
            else:
                messages.error(request, u'Восстановление пароля не увенчались успехом.')
                return self.form_invalid(form)
        else:
            messages.error(request, u'Ссылка для изменения пароля больше не действительна.')
            return self.form_invalid(form)
