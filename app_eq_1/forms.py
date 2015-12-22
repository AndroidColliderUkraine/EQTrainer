from django 				import forms

from .models 				import Course
from .models 				import Lesson
from .models 				import Article
from .models 				import UserCourse
from .models 				import Action
from .models 				import EmotionalState
from .models import WeeklyReport
from .models import MonthlyReport
from .models import Training
from redactor.widgets import RedactorEditor


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
           'text': RedactorEditor(),
        }


class UserCourseForm(forms.ModelForm):
    class Meta:
        model = UserCourse
        fields = '__all__'


class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = '__all__'


class EmotionalStateForm(forms.ModelForm):
    class Meta:
        model = EmotionalState
        fields = '__all__'


class WeeklyReportForm(forms.ModelForm):
    class Meta:
        model = WeeklyReport
        fields = '__all__'


class MonthlyReportForm(forms.ModelForm):
    class Meta:
        model = MonthlyReport
        fields = '__all__'


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = '__all__'
