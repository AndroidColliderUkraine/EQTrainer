from tastypie.resources 		import ModelResource
from .models 					import Course
from tastypie.authorization 	import Authorization
from tastypie.validation 		import FormValidation


class EntryResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'course'
        # authorization = Authorization()
        # excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        # fields = ['username', 'first_name', 'last_name', 'last_login']
        # allowed_methods = ['get']
        always_return_data = True
        authorization = Authorization()