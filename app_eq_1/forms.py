# -*- coding: utf-8 -*-
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
from django import forms


class UserRegistrationForm(forms.ModelForm):

    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        help_text="Enter the same password as above, for verification.")

    class Meta:
        model = User
        fields = ("username", "email")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


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
    text = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 120, 'rows': 25}),
        help_text=mark_safe("<xmp>Використовувати наступне:\n"
                            "&nbsp; - пробіл\n"
                            "<br> - перехід на наступний рядок\n"
                            "<b>текст</> - жирний шрифт\n"
                            "<i>текст</i> - курсив шрифт\n"
                            "<u>текст</u> - підкреслений шрифт\n"
                            "</xmp>")
    )

    class Meta:
        model = Course
        fields = '__all__'
        exclude = ['tags']


class LessonForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 120, 'rows': 25}),
        help_text=mark_safe("<xmp>Використовувати наступне:\n"
                            "&nbsp; - пробіл\n"
                            "<br> - перехід на наступний рядок\n"
                            "<b>текст</> - жирний шрифт\n"
                            "<i>текст</i> - курсив шрифт\n"
                            "<u>текст</u> - підкреслений шрифт\n"
                            "<a href='http://www.emocontrol.net/'>EmoControl</a> - посилання\n"
                            "</xmp>")
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
    text = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 120, 'rows': 25}),
        help_text=mark_safe("<xmp>Використовувати наступне:\n"
                            "&nbsp; - пробіл\n"
                            "<br> - перехід на наступний рядок\n"
                            "<b>текст</> - жирний шрифт\n"
                            "<i>текст</i> - курсив шрифт\n"
                            "<u>текст</u> - підкреслений шрифт\n"
                            "</xmp>")
    )

    class Meta:
        model = Training
        fields = '__all__'


class ConclusionsForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 120, 'rows': 25}),
        help_text=mark_safe("<xmp>Використовувати наступне:\n"
                            "&nbsp; - пробіл\n"
                            "<br> - перехід на наступний рядок\n"
                            "<b>текст</> - жирний шрифт\n"
                            "<i>текст</i> - курсив шрифт\n"
                            "<u>текст</u> - підкреслений шрифт\n"
                            "</xmp>")
    )

    class Meta:
        model = Conclusions
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]


class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(label="Email", max_length=254)


class SetPasswordForm(forms.Form):
    """
    A form that lets a user change set their password without entering the old
    password
    """
    error_messages = {
        'password_mismatch': (u"Два поля пароля не совпадают."),
        }
    new_password1 = forms.CharField(label=("New password"),
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=("New password confirmation"),
                                    widget=forms.PasswordInput)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                    )
        return password2