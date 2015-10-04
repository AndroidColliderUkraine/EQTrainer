from django.conf.urls 			import include, url
from django.contrib 			import admin

from tastypie.api 				import Api
from app_eq_1.api 				import EntryResource


v1_api = Api(api_name='v1')
v1_api.register(EntryResource())

urlpatterns = [
    # Examples:
    # url(r'^$', 'eq.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app_eq_1.views.home', name='home'),
    url(r'^profile$', 'app_eq_1.views.profile', name='profile'),

    url(r'^api/', include(v1_api.urls)),

]
