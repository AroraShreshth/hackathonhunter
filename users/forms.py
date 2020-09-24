from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Snippet
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        # widget=forms.TextInput(attrs={
        #     'class': 'input',
        #     'placeholder': 'e.g. awesome'
        # }
        # )
    )

    # username = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         'class': 'input',
    #         'autofocus': True,
    #         'placeholder': 'Username'
    #     }
    #     ))
    # password = forms.CharField(
    #     widget=forms.PasswordInput(attrs={
    #         'class': 'input',
    #         'placeholder': '*******'
    #     }
    #     ))

    captcha = ReCaptchaField(
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.85,
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email',  'password1', 'password2']


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


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class SearchForm(forms.ModelForm):
    query = forms.TextInput()

    class Meta:
        fields = ['query']
