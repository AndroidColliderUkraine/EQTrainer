from django.conf.urls 			import include, url, patterns
from django.contrib 			import admin

from tastypie.api 				import Api
from app_eq_1.api 				import CourseResource
from app_eq_1.api 				import LessonResource
from app_eq_1.api 				import ArticleResource
from app_eq_1.api 				import UserCourseResource
from app_eq_1.api 				import ActionResource
from app_eq_1.api 				import EmotionalStateResource
from app_eq_1.api 				import UserResource
from app_eq_1.api import WeeklyReportResource
from app_eq_1.api import MonthlyReportResource
from app_eq_1.api import TrainingResource
import settings

v1_api = Api(api_name='v1')
v1_api.register(CourseResource())
v1_api.register(LessonResource())
v1_api.register(ArticleResource())
v1_api.register(UserCourseResource())
v1_api.register(ActionResource())
v1_api.register(EmotionalStateResource())
v1_api.register(UserResource())
v1_api.register(WeeklyReportResource())
v1_api.register(MonthlyReportResource())
v1_api.register(TrainingResource())

urlpatterns = [
    # Examples:
    # url(r'^$', 'eq.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^tinymce/', include('tinymce.urls')),
    url(r'^lawyer_page$', 'app_eq_1.views.lawyer_page', name='lawyer_page'),
    url(r'^report_graph$', 'app_eq_1.views.report_graph', name='report_graph'),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app_eq_1.views.home', name='home'),
    # url(r'^profile/home$', 'app_eq_1.views.profile_home', name='profile_home'),
    url(r'^profile/mycourses$', 'app_eq_1.views.profile_mycourses', name='profile_mycourses'),
    url(r'^profile/myusercourse', 'app_eq_1.views.profile_myusercourse', name='profile_myusercourse'),
    url(r'^profile/mydaybook', 'app_eq_1.views.profile_mydaybook', name='profile_mydaybook'),

    # url(r'^profile/courses$', 'app_eq_1.views.profile_courses', name='profile_courses'),
    # url(r'^profile/articles$', 'app_eq_1.views.profile_articles', name='profile_articles'),
    # url(r'^profile$', 'app_eq_1.views.profile', name='profile'),


    url(r'^course/', 'app_eq_1.views.course', name='course'),
    url(r'^courses/', 'app_eq_1.views.courses', name='courses'),
    url(r'^article/', 'app_eq_1.views.article', name='article'),
    url(r'^articles/', 'app_eq_1.views.articles', name='articles'),
    url(r'^trener/', 'app_eq_1.views.trener', name='trener'),
    url(r'^about/', 'app_eq_1.views.about', name='about'),



    url(r'^api/', include(v1_api.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    # url(r'^auth/', include('djoser.urls')),


    url(r'^subscribe_course/', 'app_eq_1.views.subscribe_course', name='subscribe_course'),
    url(r'^unsubscribe_course/', 'app_eq_1.views.unsubscribe_course', name='unsubscribe_course'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT})
]
