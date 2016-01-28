from django.contrib 		import admin

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

from django.contrib.auth.admin import UserAdmin

UserAdmin.list_display = ('username', 'id', 'email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')


class CourseAdmin(admin.ModelAdmin):
	list_display = ['id', "__unicode__", "tags", "state", "price", "updated", "deleted"]
	form = CourseForm


class LessonAdmin(admin.ModelAdmin):
	list_display = ['id', "__unicode__", "course", "state", "tags", "updated", "deleted"]
	form = LessonForm


class ArticleAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "state", "tags", "updated", "deleted"]
	form = ArticleAdminForm


class UserCourseAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "user", "course", "status",  "updated", "deleted"]
	form = UserCourseForm


class ActionAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "user_course", "lesson", "updated", "deleted"]
	form = ActionForm


class EmotionalStateAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "user", "emotion", "activity", "subjectivity", "confidence", "updated", "deleted"]
	form = EmotionalStateForm


class WeeklyReportAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "user", "updated", "deleted"]
	form = WeeklyReportForm


class MonthlyReportAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "user", "updated", "deleted"]
	form = MonthlyReportForm


class TrainingAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "updated", "deleted"]
	form = TrainingForm


class ConclusionsAdmin(admin.ModelAdmin):
	list_display = ["id", "text", "emotion", "activity", "updated", "deleted"]
	form = ConclusionsForm

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