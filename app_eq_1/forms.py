from django 				import forms
from django.utils.safestring import mark_safe

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
from redactor.widgets import RedactorEditor
from django.contrib.auth.models 	import User
from django.core.files.images import get_image_dimensions


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'subscribe_mailing']

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        # validate default image
        print 'AVATAR', type(avatar), avatar
        if not avatar or len(avatar) == 0:
            return 'avatars/default.png'
        try:
            w, h = get_image_dimensions(avatar)

            # #validate dimensions
            # max_width = max_height = 128
            # if w > max_width or h > max_height:
            #     avatar = self.autoresize_image(avatar)
            #     # raise forms.ValidationError(
            #     #     u'Please use an image that is '
            #     #      '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')

            #validate file size
            if len(avatar) > (20000 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20M.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        exclude = ['tags']


class LessonForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea,
        help_text=mark_safe("<xmp>You can use link in text: <a href='http://www.emocontrol.net/'>EmoControl</a></xmp>")
    )

    class Meta:
        model = Lesson
        fields = '__all__'
        exclude = ['tags']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['tags']
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


class ConclusionsForm(forms.ModelForm):
    class Meta:
        model = Conclusions
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]


