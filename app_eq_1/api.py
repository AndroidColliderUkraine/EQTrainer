from tastypie.resources 		import ModelResource
from .models 					import Course
from .models 					import Lesson
from .models 					import Article
from .models 					import UserCourse
from .models 					import Action
from .models 					import EmotionalState
from .models import WeeklyReport
from .models import MonthlyReport
from .models import Training
from tastypie.authorization 	import Authorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.validation 		import FormValidation
from datetime                   import datetime
from tastypie import fields
from django.contrib.auth.models 	import User


class UserResource(ModelResource):

    class Meta:
        queryset = User.objects.all()
        resource_name = 'User'
        # excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        fields = ['id', 'last_login']
        # allowed_methods = ['get']
        filtering = {
            # 'User': ALL_WITH_RELATIONS,
            'id': ALL,
            'username': ALL,
            'updated': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
        always_return_data = True
        authorization = Authorization()


class WeeklyReportResource(ModelResource):
    def dehydrate(self, bundle):
        deleted_objects = WeeklyReport.objects.filter(deleted=True).all().values('id')
        bundle.data['deleted_objects'] = deleted_objects
        return bundle

    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = WeeklyReport.objects.filter(deleted=False).all()
        resource_name = 'WeeklyReport'
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'updated': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
        always_return_data = True
        authorization = Authorization()


class MonthlyReportResource(ModelResource):
    def dehydrate(self, bundle):
        deleted_objects = MonthlyReport.objects.filter(deleted=True).all().values('id')
        bundle.data['deleted_objects'] = deleted_objects
        return bundle

    class Meta:
        queryset = MonthlyReport.objects.filter(deleted=False).all()
        resource_name = 'MonthlyReport'
        filtering = {
            'updated': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
        always_return_data = True
        authorization = Authorization()


class TrainingResource(ModelResource):

    def dehydrate(self, bundle):
        deleted_objects = Training.objects.filter(deleted=True).all().values('id')
        bundle.data['deleted_objects'] = deleted_objects
        return bundle

    class Meta:
        queryset = Training.objects.filter(deleted=False).all()
        resource_name = 'Training'
        filtering = {
            'updated': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
        always_return_data = True
        authorization = Authorization()


class CourseResource(ModelResource):
    def dehydrate(self, bundle):
        deleted_objects = Course.objects.filter(deleted=True).all().values('id')
        bundle.data['deleted_objects'] = deleted_objects
        return bundle

    class Meta:
        queryset = Course.objects.filter(deleted=False).all()
        resource_name = 'Course'
        # excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        # fields = ['username', 'first_name', 'last_name', 'last_login']
        # allowed_methods = ['get']
        filtering = {
            'updated': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
        always_return_data = True
        authorization = Authorization()


class LessonResource(ModelResource):
    def dehydrate(self, bundle):
        deleted_objects = Lesson.objects.filter(deleted=True).all().values('id')
        bundle.data['deleted_objects'] = deleted_objects
        return bundle

    class Meta:
        queryset = Lesson.objects.filter(deleted=False).all()
        resource_name = 'Lesson'
        # excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        # fields = ['username', 'first_name', 'last_name', 'last_login']
        # allowed_methods = ['get']
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'id': ALL,
            'updated': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
        always_return_data = True
        authorization = Authorization()


class ArticleResource(ModelResource):
    def dehydrate(self, bundle):
        deleted_objects = Article.objects.filter(deleted=True).all().values('id')
        bundle.data['deleted_objects'] = deleted_objects
        return bundle

    class Meta:
        queryset = Article.objects.filter(deleted=False).all()
        resource_name = 'Article'
        # excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        # fields = ['username', 'first_name', 'last_name', 'last_login']
        # allowed_methods = ['get']
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'updated': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
        always_return_data = True
        authorization = Authorization()


class UserCourseResource(ModelResource):

    def dehydrate(self, bundle):
        deleted_objects = UserCourse.objects.filter(deleted=True).all().values('id')
        bundle.data['deleted_objects'] = deleted_objects
        # bundle.data['course_id'] = bundle.obj.course_id.id
        # print '////////', bundle.obj.course_id
        bundle.data['courseid'] = bundle.obj.course_id
        return bundle

    user = fields.ForeignKey(UserResource, 'user', full=True)
    courseid = fields.ForeignKey(CourseResource, 'course', full=True)
    # course_id = fields.IntegerField(attribute='Course_id', null=True)

    class Meta:
        queryset = UserCourse.objects.filter(deleted=False).all()
        resource_name = 'UserCourse'
        # excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        # fields = ['username', 'first_name', 'last_name', 'last_login']
        # allowed_methods = ['get']
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'courseid': ALL,
            'id': ALL,
            'updated': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
        always_return_data = True
        authorization = Authorization()


class ActionResource(ModelResource):
    def dehydrate(self, bundle):
        deleted_objects = Action.objects.filter(deleted=True).all().values('id')
        bundle.data['deleted_objects'] = deleted_objects
        return bundle

    lesson = fields.ForeignKey(LessonResource, 'lesson', full=True)
    user_course = fields.ForeignKey(UserCourseResource, 'user_course', full=True)

    class Meta:
        queryset = Action.objects.filter(deleted=False).all()
        resource_name = 'Action'
        # excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        # fields = ['id', 'lesson']
        # allowed_methods = ['get']
        filtering = {
            'id': ALL,
            'user': ALL_WITH_RELATIONS,
            # 'UserCourse': ALL_WITH_RELATIONS,
            'user_course': ALL_WITH_RELATIONS,
            'updated': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
        always_return_data = True
        authorization = Authorization()


class EmotionalStateResource(ModelResource):
    def dehydrate(self, bundle):
        deleted_objects = EmotionalState.objects.filter(deleted=True).all().values('id')
        bundle.data['deleted_objects'] = deleted_objects
        return bundle

    user = fields.ForeignKey(UserResource, 'user', full=True)
    class Meta:
        queryset = EmotionalState.objects.filter(deleted=False).all()
        resource_name = 'EmotionalState'
        # excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        # fields = ['username', 'first_name', 'last_name', 'last_login']
        # allowed_methods = ['get']
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'updated': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
        always_return_data = True
        authorization = Authorization()
