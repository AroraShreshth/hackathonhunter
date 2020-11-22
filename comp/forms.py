from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import (
    Event, Announcement, ApplicationQuestion,
    TimelineEvent, Judge, FAQ, SponsorType, Sponsor, PrizeType, Prize)
from users.models import City
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from dal import autocomplete


class EventAbout(forms.ModelForm):

    startdate = forms.DateField(
        localize=True,
        label='Start Date',
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'class': 'form-control',
                'required': 'true',
            }
        ),
    )

    enddate = forms.DateField(
        localize=True,
        label='End Date',
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'class': 'form-control',
                'required': 'true',
            }
        ),
    )

    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.75,
            }
        )
    )

    class Meta:
        model = Event
        fields = ['name', 'tagline', 'startdate',
                  'enddate', 'organiser_admin', 'captcha']


class EventDetailForm(forms.ModelForm):

    description = forms.CharField(
        max_length=5000,
        min_length=100,
        label='Description',
        widget=forms.Textarea(
            attrs={"rows": 15, "cols": 20, "required": True})
    )

    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.75,
            }
        )
    )

    class Meta:
        model = Event
        fields = ['is_online', 'is_team_comp',
                  'women_only', 'application_review', 'description', 'captcha']
        labels = {
            'is_online': 'Online Event',
            'is_team_comp': 'Team Based Event',
            'women_only': 'Women Only Event',
            'application_review': 'Application Review'
        }


class EventOfflineForm(forms.ModelForm):

    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.75,
            }
        )
    )

    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='city-autocomplete',
            attrs={
                'data-placeholder': 'City Organised In',
                'data-minimum-input-length': 0,
            },
        )
    )

    class Meta:
        model = Event
        fields = ['address', 'city',
                  # 'latitude', 'longitude',
                  'captcha'
                  ]


class EventTeamForm(forms.ModelForm):

    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.75,
            }
        )
    )

    # Limits to both of these no.s
    class Meta:
        model = Event
        fields = ['team_size', 'team_min', 'captcha']
        labels = {
            'team_size': 'Max Team Size',
            'team_min': 'Min Team Size'
        }


class EventLinksForm(forms.ModelForm):

    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.75,
            }
        )
    )

    class Meta:
        model = Event
        fields = ['website', 'twitter', 'facebook',
                  'linkedin', 'medium', 'instagram', 'coc', 'captcha']
        labels = {
            'website': 'Website Link',
            'twitter': 'Twitter Link',
            'linkedin': 'Linkedin Link',
            'medium': 'Medium Link',
            'instagram': 'Instagram Link',
            'coc': 'Code of Conduct Link',
        }


class ApplicationQuestionForm(forms.ModelForm):

    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.75,
            }
        )
    )

    class Meta:
        model = ApplicationQuestion
        fields = ['question', 'required', 'types', 'captcha']

        labels = {
            'required': 'Required',
            'types': 'Response of Question',
            'question': 'Question'
        }


class TimelineEventForm(forms.ModelForm):
    name = forms.CharField(min_length=15, label='Name')

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 4,
                "cols": 20,
                "required": True
            }
        ),
        max_length=500,
        min_length=20,
    )

    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.75,
            }
        )
    )

    class Meta:
        model = TimelineEvent
        fields = ['name', 'date', 'important', 'description', 'captcha']
        labels = {
            'date': 'Date and Time',
            'description': 'Description',
        }


class CreateFAQForm(forms.ModelForm):
    question = forms.CharField(min_length=15, label='Question')
    answer = forms.CharField(min_length=15, label='Answer')

    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.75,
            }
        )
    )

    class Meta:
        model = FAQ
        fields = ['question', 'answer', 'captcha']
