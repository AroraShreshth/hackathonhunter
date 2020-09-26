from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile, Snippet
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from django.contrib.auth.forms import AuthenticationForm


class UserRegisterForm(UserCreationForm):
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
                'class': 'party'
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

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ProfileGTForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['gender', 'shirt_size']


class ProfileAboutForm(forms.ModelForm):
    bio = forms.CharField(
        max_length=500,
        min_length=20,
        label='Tell Us About Yourself',
        widget=forms.Textarea
    )

    image = forms.FileField(required=True, label='Profile Image', widget=forms.FileInput(attrs={
        'data-empty-message': 'Please upload Profile Image'
    }))

    class Meta:
        model = Profile
        fields = ['image', 'gender', 'bio']
        labels = {
            'image': 'Profile Image',
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
        widget=forms.TextInput(attrs={'type': 'number'}),
        label='Mail OTP'
    )
