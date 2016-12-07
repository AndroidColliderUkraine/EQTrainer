from django.contrib 		import admin
from django.contrib.auth.models import User
from .forms 				import CourseForm
from .forms 				import LessonForm
from .forms 				import ArticleAdminForm
from .forms 				import UserCourseForm
from .forms 				import ActionForm
from .forms 				import EmotionalStateForm
from .forms import WeeklyReportForm
from .forms import MonthlyReportForm
from .forms import TrainingForm
from .forms import ConclusionsForm
from .forms import UserProfileForm

from .models 				import Course
from .models 				import Lesson
from .models 				import Article
from .models 				import UserCourse
from .models 				import Action
from .models 				import EmotionalState
from .models import WeeklyReport
from .models import MonthlyReport
from .models import Training
from .models import Conclusions
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin
from helps import forced_login
from django.shortcuts import redirect


# UserAdmin.list_display = ('username', 'id', 'email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')


class EqUserAdmin(UserAdmin):
    actions = [
        'impersonate_user',
    ]
    list_display = ('username', 'id', 'email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')

    def impersonate_user(self, request, queryset):
        if queryset.count() != 1:
            # messages.error(request, "Can impersonate only one user")
            self.message_user(request, "Can impersonate only one user")
            return
        person = queryset.all()[0]
        forced_login(request, person, False)
        return redirect('/')

    impersonate_user.short_description = "Impersonate user"

    def get_actions(self, request):
        actions = super(EqUserAdmin, self).get_actions(request)
        return actions

    def __init__(self, *args, **kwargs):
        super(EqUserAdmin, self).__init__(*args, **kwargs)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', "user", "avatar", "subscribe_mailing"]
    form = UserProfileForm


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', "__unicode__", "state", "price", "price_rub", "price_dol", "updated", "deleted"]
    list_filter = ('deleted', 'price', 'state', )
    search_fields = ["id", "name", "text"]
    form = CourseForm


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', "__unicode__", "course", "state", "updated", "deleted"]
    search_fields = ["id", "name", "text"]
    list_filter = (
        ('course', admin.RelatedOnlyFieldListFilter),
        'deleted',
    )
    form = LessonForm

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('course',)
        return self.readonly_fields


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "state", "updated", "deleted"]
    form = ArticleAdminForm


class UserCourseAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "user", "course", "status", "created", "updated", "deleted"]
    search_fields = ["id", "user__email", "course__name"]
    list_filter = ("status", "created")
    form = UserCourseForm

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('user', 'course', 'last_lesson')
        return self.readonly_fields


class ActionAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "user_course", "lesson", "updated", "deleted"]
    form = ActionForm


class EmotionalStateAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "user", "emotion", "activity", "subjectivity", "confidence", "updated", "deleted"]
    search_fields = ["user__email", "emotion", "activity"]
    list_filter = ("updated", "emotion", "activity")
    form = EmotionalStateForm


class WeeklyReportAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "id", "user", "date_start", "date_end", "updated", "deleted"]
    search_fields = ["user__email"]
    form = WeeklyReportForm


class MonthlyReportAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "id", "user", "date_start", "date_end", "updated", "deleted"]
    search_fields = ["user__email"]
    form = MonthlyReportForm


class TrainingAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "updated", "deleted"]
    search_fields = ["name", "text"]
    form = TrainingForm


class ConclusionsAdmin(admin.ModelAdmin):
    list_display = ["id", "text", "emotion", "activity", "updated", "deleted"]
    search_fields = ["id", "text", "emotion", "activity"]
    form = ConclusionsForm

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('emotion', 'activity')
        return self.readonly_fields

admin.site.unregister(User)
admin.site.register(User, EqUserAdmin)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(UserCourse, UserCourseAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(EmotionalState, EmotionalStateAdmin)
admin.site.register(WeeklyReport, WeeklyReportAdmin)
admin.site.register(MonthlyReport, MonthlyReportAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Conclusions, ConclusionsAdmin)