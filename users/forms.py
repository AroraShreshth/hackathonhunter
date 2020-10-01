from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile, Snippet
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from django.contrib.auth.forms import AuthenticationForm


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


class BioForm(forms.ModelForm):
    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.75,
            }
        )
    )

    class Meta:
        model = Profile
        fields = ['bio']


class ProfileGTForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['gender', 'shirt_size']


class ProfileAboutForm(forms.ModelForm):
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

    class Meta:
        model = Profile
        fields = ['dob', 'gender', 'bio', 'captcha']
        labels = {
            'dob': 'Date of Birth',
            'gender': 'Gender',
        }


class ProfileEducationForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['no_formal_education', 'degree_type',
                  'grad_year', 'field_of_study']


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


class ProfileResumeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['resume']


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
