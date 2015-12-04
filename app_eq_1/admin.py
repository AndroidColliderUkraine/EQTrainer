from django.contrib 		import admin

from .forms 				import CourseForm
from .forms 				import LessonForm
from .forms 				import ArticleForm
from .forms 				import UserCourseForm
from .forms 				import ActionForm
from .forms 				import EmotionalStateForm
from .forms import WeeklyReportForm
from .forms import MonthlyReportForm
from  .forms import TrainingForm

from .models 				import Course
from .models 				import Lesson
from .models 				import Article
from .models 				import UserCourse
from .models 				import Action
from .models 				import EmotionalState
from .models import WeeklyReport
from .models import MonthlyReport
from  .models import Training

from django.contrib.auth.admin import UserAdmin

UserAdmin.list_display = ('username', 'id', 'email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')


class CourseAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "tags", "state", "price", "updated",]
	form = CourseForm


class LessonAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "course", "state", "tags", "updated",]	
	form = LessonForm


class ArticleAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "state", "tags", "updated",]	
	form = ArticleForm


class UserCourseAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "user", "course", "paid", "status",  "updated",]	
	form = UserCourseForm


class ActionAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "user_course", "lesson", "updated",]	
	form = ActionForm


class EmotionalStateAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "user", "emotion", "activity", "subjectivity", "confidence", "updated",]
	form = EmotionalStateForm


class WeeklyReportAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "user", "date",]
	form = WeeklyReportForm


class MonthlyReportAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "user", "date",]
	form = MonthlyReportForm


class TrainingAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "date",]
	form = TrainingForm

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(UserCourse, UserCourseAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(EmotionalState, EmotionalStateAdmin)
admin.site.register(WeeklyReport, WeeklyReportAdmin)
admin.site.register(MonthlyReport, MonthlyReportAdmin)
admin.site.register(Training, TrainingAdmin)