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
    url(r'^profile$', 'app_eq_1.views.profile', name='profile'),
    url(r'^course/', 'app_eq_1.views.course', name='course'),
    url(r'^article/', 'app_eq_1.views.article', name='article'),

    url(r'^api/', include(v1_api.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^auth/', include('djoser.urls')),


    url(r'^subscribe_course/', 'app_eq_1.views.subscribe_course', name='subscribe_course'),
    url(r'^unsubscribe_course/', 'app_eq_1.views.unsubscribe_course', name='unsubscribe_course'),

]
