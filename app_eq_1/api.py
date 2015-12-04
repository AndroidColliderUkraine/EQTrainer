from tastypie.resources 		import ModelResource
from .models 					import Course
from .models 					import Lesson
from .models 					import Article
from .models 					import UserCourse
from .models 					import Action
from .models 					import EmotionalState
from tastypie.authorization 	import Authorization
from tastypie.validation 		import FormValidation
from datetime                   import datetime

class CourseResource(ModelResource):
    def dehydrate(self, bundle):
        bundle.data['updated'] = str(bundle.obj.updated.strftime("%s"))
        return bundle

    def hydrate(self, bundle):
        # print "!!!!!!!!!!!!!!!!!!!!!!!!!!!1 date:", bundle.obj.updated
        # print "!!!!!!!!!!!!!!!!!!!!!!!!!!!2 date:", str(datetime.fromtimestamp(int( str( bundle.obj.updated) )))
        # bundle.data['updated'] = str(datetime.fromtimestamp(int( str( bundle.obj.updated) )))
        # bundle.data['updated'] = '2015-10-21 12:23:25.167657'
        return bundle

    class Meta:
        queryset = Course.objects.all()
        resource_name = 'Course'
        # authorization = Authorization()
        # excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        # fields = ['username', 'first_name', 'last_name', 'last_login']
        # allowed_methods = ['get']
        always_return_data = True
        authorization = Authorization()


class LessonResource(ModelResource):
    def dehydrate(self, bundle):
        bundle.data['updated'] = str(bundle.obj.updated.strftime("%s"))
        return bundle

    class Meta:
        queryset = Lesson.objects.all()
        resource_name = 'Lesson'
        # authorization = Authorization()
        # excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        # fields = ['username', 'first_name', 'last_name', 'last_login']
        # allowed_methods = ['get']
        always_return_data = True
        authorization = Authorization()


class ArticleResource(ModelResource):
    def dehydrate(self, bundle):
        bundle.data['updated'] = str(bundle.obj.updated.strftime("%s"))
        return bundle

    class Meta:
        queryset = Article.objects.all()
        resource_name = 'Article'
        # authorization = Authorization()
        # excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        # fields = ['username', 'first_name', 'last_name', 'last_login']
        # allowed_methods = ['get']
        always_return_data = True
        authorization = Authorization()


class UserCourseResource(ModelResource):
    def dehydrate(self, bundle):
        bundle.data['updated'] = str(bundle.obj.updated.strftime("%s"))
        return bundle

    class Meta:
        queryset = UserCourse.objects.all()
        resource_name = 'UserCourse'
        # authorization = Authorization()
        # excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        # fields = ['username', 'first_name', 'last_name', 'last_login']
        # allowed_methods = ['get']
        always_return_data = True
        authorization = Authorization()


class ActionResource(ModelResource):
    def dehydrate(self, bundle):
        bundle.data['updated'] = str(bundle.obj.updated.strftime("%s"))
        return bundle

    class Meta:
        queryset = Action.objects.all()
        resource_name = 'Action'
        # authorization = Authorization()
        # excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        # fields = ['username', 'first_name', 'last_name', 'last_login']
        # allowed_methods = ['get']
        always_return_data = True
        authorization = Authorization()


class EmotionalStateResource(ModelResource):
    def dehydrate(self, bundle):
        bundle.data['updated'] = str(bundle.obj.updated.strftime("%s"))
        return bundle

    class Meta:
        queryset = EmotionalState.objects.all()
        resource_name = 'EmotionalState'
        # authorization = Authorization()
        # excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        # fields = ['username', 'first_name', 'last_name', 'last_login']
        # allowed_methods = ['get']
        always_return_data = True
        authorization = Authorization()
