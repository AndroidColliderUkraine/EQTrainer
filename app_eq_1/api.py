from tastypie.resources 		import ModelResource
from .models 					import Course
from .models 					import Lesson
from .models 					import Article
from .models 					import UserCourse
from .models 					import Action
from .models 					import EmotionalState
from tastypie.authorization 	import Authorization
from tastypie.validation 		import FormValidation


class CourseResource(ModelResource):
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
    class Meta:
        queryset = EmotionalState.objects.all()
        resource_name = 'EmotionalState'
        # authorization = Authorization()
        # excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        # fields = ['username', 'first_name', 'last_name', 'last_login']
        # allowed_methods = ['get']
        always_return_data = True
        authorization = Authorization()
