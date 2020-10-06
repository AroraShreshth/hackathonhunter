from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile, Snippet, Work, Link, Institute, FieldofStudy
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from django.contrib.auth.forms import AuthenticationForm
import datetime
from dal import autocomplete


class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        # for fieldname in ['username', 'password1', 'password2']:
        self.fields['password1'].help_text = 'Please keep your password dissimilar from your other info, 8 Characterers Minium, Not entirely Numeric, also please don\'t use common passwords for security purposes'
    email = forms.EmailField()

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                "Entered Email already exists ! Please Login")
        return self.cleaned_data

    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.75,
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email',  'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.75,
            }
        )
    )

    class Meta:
        fields = ['username', 'password', 'captcha']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class NameForm(forms.ModelForm):
    first_name = forms.CharField(min_length=3)
    last_name = forms.CharField(min_length=3)
    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.75,
            }
        )
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'captcha']


class ShirtSizeGenderForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender', 'shirt_size']


class BioForm(forms.Form):
    # Used in Profile Setup
    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.75,
            }
        )
    )
    bio = forms.CharField(
        max_length=5000,
        min_length=20,
        label='Bio',
        widget=forms.Textarea
    )


class ProfileGTForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['gender', 'shirt_size']


class ProfileAboutForm(forms.ModelForm):
    # used in Welcome Setup
    bio = forms.CharField(
        max_length=500,
        min_length=20,
        label='Tell Us About Yourself (min 20 letters)',
        widget=forms.Textarea
    )
    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.75,
            }
        )
    )

    dob = forms.DateField(
        localize=True,
        label='Date of Birth',
        widget=forms.DateInput(
            format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
    )

    # def clean(self):
    #     dob_data = self.cleaned_data.get('dob')
    #     t = datetime.datetime.now() - datetime.timedelta(days=13*365)
    #     if dob_data < t.date():
    #         raise forms.ValidationError(
    #             'You should be older than 13 years to signup on the application')

    #     return self.cleaned_data

    class Meta:
        model = Profile
        fields = ['dob', 'gender', 'bio', 'captcha']
        labels = {
            'dob': 'Date of Birth',
            'gender': 'Gender',
        }


class ProfileEducationForm(forms.ModelForm):
    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.75,
            }
        )
    )
    grad_year = forms.DateField(
        localize=True,
        label='Graduation Year',
        widget=forms.DateInput(
            format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
    )

    institute = forms.ModelChoiceField(
        queryset=Institute.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='institute-autocomplete',
            attrs={
                'data-placeholder': 'Institute',
                'data-minimum-input-length': 0,
                'class': 'dropdown'
            },
        )
    )
    field_of_study = forms.ModelChoiceField(
        queryset=FieldofStudy.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='fieldofstudy-autocomplete',
            attrs={
                'data-placeholder': 'Field of Study',
                'data-minimum-input-length': 0,
            },
        ),
    )

    class Meta:
        model = Profile
        fields = ['degree_type',
                  'course_length',
                  'field_of_study',
                  'institute',
                  'grad_year',
                  'captcha']
        labels = {
            'course_length': 'Duration of Academic Course'
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class SearchForm(forms.ModelForm):
    query = forms.TextInput()

    class Meta:
        fields = ['query']


class EmailVerifyForm(forms.Form):
    OTP = forms.CharField(
        max_length=6,
        min_length=6,
        widget=forms.TextInput(attrs={'type': 'number', 'min': '100000'}),
        label='Mail OTP'
    )
    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.75,
            }
        )
    )


class ProfileExpForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['resume', 'skill']


class ProfileWorkForm(forms.ModelForm):
    start = forms.DateField(
        localize=True,
        label='Work Start',
        widget=forms.DateInput(
            format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
    )
    end = forms.DateField(
        localize=True,
        label='Work End',
        widget=forms.DateInput(
            format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
    )

    class Meta:
        model = Work
        fields = ['employer', 'role',
                  'start', 'end', 'currently_working', 'description']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'emergency_contact_name']


class ContactEmergencyForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['emergency_contact_name', 'emergency_phone']


class PhoneVerifyForm(forms.ModelForm):
    OTP = forms.CharField(
        max_length=6,
        min_length=6,
        widget=forms.TextInput(attrs={'type': 'number', 'min': '100000'}),
        label='Phone OTP'
    )
    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.75,
            }
        )
    )
