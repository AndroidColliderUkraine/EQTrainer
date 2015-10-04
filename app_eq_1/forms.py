from django 				import forms

from .models 				import Course
from .models 				import Lesson
from .models 				import Article
from .models 				import UserCourse
from .models 				import Action
from .models 				import EmotionalState


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
