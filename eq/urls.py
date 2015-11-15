from django.conf.urls 			import include, url
from django.contrib 			import admin

from tastypie.api 				import Api
from app_eq_1.api 				import CourseResource
from app_eq_1.api 				import LessonResource
from app_eq_1.api 				import ArticleResource
from app_eq_1.api 				import UserCourseResource
from app_eq_1.api 				import ActionResource
from app_eq_1.api 				import EmotionalStateResource

v1_api = Api(api_name='v1')
v1_api.register(CourseResource())
v1_api.register(LessonResource())
v1_api.register(ArticleResource())
v1_api.register(UserCourseResource())
v1_api.register(ActionResource())
v1_api.register(EmotionalStateResource())

urlpatterns = [
    # Examples:
    # url(r'^$', 'eq.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app_eq_1.views.home', name='home'),
    # url(r'^profile/home$', 'app_eq_1.views.profile_home', name='profile_home'),
    url(r'^profile/mycourses$', 'app_eq_1.views.profile_mycourses', name='profile_mycourses'),
    url(r'^profile/mycourse', 'app_eq_1.views.profile_mycourse', name='profile_mycourse'),

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
    url(r'^auth/', include('djoser.urls')),


    url(r'^subscribe_course/', 'app_eq_1.views.subscribe_course', name='subscribe_course'),
    url(r'^unsubscribe_course/', 'app_eq_1.views.unsubscribe_course', name='unsubscribe_course'),

]
