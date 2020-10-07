from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import (UserRegisterForm, UserUpdateForm, ProfileUpdateForm,
                    SearchForm, NameForm, EmailVerifyForm, ProfileAboutForm, ProfileEducationForm, ProfileExpForm, ProfileWorkForm, UserLoginForm, BioForm, ShirtSizeGenderForm)
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.views.generic.base import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from users.models import Snippet, Profile, Institute, Work, Link, Skill, FieldofStudy, City
from django.contrib.auth import views as auth_views
from vacc.settings import website_name
from django.core.mail import send_mail
import random
import re
import markdown
from dal import autocomplete


def homepage(request):
    return render(request, 'unlogged/index.html', {'title': '', 'website_name': website_name})


class PrivacyPolicy(TemplateView):
    template_name = 'unlogged/privacy-policy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['website_name'] = website_name
        context['title'] = 'Privacy Policy'
        return context


class TermsofService(TemplateView):
    template_name = 'unlogged/terms-of-service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['website_name'] = website_name
        context['title'] = 'Terms of Service'
        return context


class Help(TemplateView):
    template_name = 'unlogged/help.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['website_name'] = website_name
        context['title'] = 'Help'
        return context


class About(TemplateView):
    template_name = 'unlogged/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['website_name'] = website_name
        context['title'] = 'About'
        return context


class Explore(TemplateView):
    template_name = 'unlogged/explore.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['website_name'] = website_name
        context['title'] = 'Explore'
        return context


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password1)
            login(request, user)
            # messages.success(
            #     request, f' {username} your account has been crreated successfully')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('dashboard-home')
        form = UserRegisterForm()
    return render(request, 'unlogged/register.html', {'website_name': website_name, 'title': 'Register', 'form': form})


class NewLoginView(auth_views.LoginView):
    template_name = 'unlogged/login.html'
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['website_name'] = website_name
        context['title'] = 'Login'
        context['form'] = UserLoginForm
        return context


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'website_name': website_name,
        'title': 'Profile',
    }

    return render(request, 'user/profile_update.html', context)


class WelcomeDone(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/welcome_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['website_name'] = website_name
        context['title'] = 'Welcome Complete'
        return context


@login_required
def welcome_about(request):
    context = {
        'website_name': website_name,
        'title': 'Welcome - Bio',
        'form': ProfileAboutForm
    }
    if request.method == 'POST':
        print('POST')
        form = ProfileAboutForm(
            request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            print('POST')
            form.save()
            # messages.success(
            #     request, f'{request.user.username} Your About Details Saved !')
            return redirect('welcome-email-verify')

    else:
        if request.user.profile.setup:
            return redirect('dashboard-home')
        if request.user.profile.bio:
            return redirect('welcome-email-verify')
        return render(request, 'dashboard/welcome_about.html', context)


@login_required
def welcome(request):
    context = {
        'website_name': website_name,
        'title': 'Welcome - Name',
        'name_form': NameForm
    }

    if request.method == 'POST':
        name_form = NameForm(request.POST, instance=request.user)

        if name_form.is_valid():
            name_form.save()
            # messages.success(
            #     request, f'{request.user.username} Name Details Saved !')
            return redirect('welcome-about')

    else:
        if request.user.profile.setup:
            return redirect('dashboard-home')
        if len(request.user.first_name) or len(request.user.last_name):
            return redirect('welcome-about')
        return render(request, 'dashboard/welcome.html', context)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'
    form = SearchForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['snippet'] = Snippet.objects.order_by('?')
        context['search_form'] = self.form
        context['website_name'] = website_name
        return context


class UserDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'user/user_detail.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        profile = self.get_object()
        context = super().get_context_data(**kwargs)
        context['snippet'] = Snippet.objects.order_by('?').first()
        context['website_name'] = website_name
        return context


# @login_required
# def DashBoard(request):
#     context = {
#         'website_name': website_name,
#         'title': 'Dashboard',
#     }
#     if not request.user.profile.setup:
#         return redirect('dashboard-welcome')
#     else:
#         return render(request, 'dashboard/home.html', context)


class DashBoard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if not request.user.profile.setup:
            return redirect('dashboard-welcome')
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['website_name'] = website_name
        context['title'] = 'Dashboard'
        return context


@login_required
def VerifyEmail(request):
    domain = re.search("@[\w.]+", request.user.email)
    context = {
        'website_name': website_name,
        'title': 'Welcome - Verify Email',
        'form': EmailVerifyForm,
        'domain': domain.group()[1:]
    }

    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':

        form = EmailVerifyForm(request.POST)

        if profile.mail_is_verified == True:
            profile.send_verification_email()
            return render(request, 'dashboard/profile_email_verify.html', context)

        if form.is_valid():
            request.user.profile.mail_is_verified == True
            print(request.POST.get('OTP'))
            print(request.user.profile.mail_otp)
            if int(request.POST.get('OTP')) == int(request.user.profile.mail_otp):
                profile.mail_is_verified = True
                profile.setup = True
                profile.mail_otp = random.randint(120930, 999999)
                profile.save()
                messages.success(
                    request, f' Hey, {request.user.username} your email has been successfully verfied !')
                return redirect('welcome-done')
            else:
                messages.error(
                    request, f' OOPS! {request.user.username} OTP provided is incorrect !')
                return render(request, 'dashboard/profile_email_verify.html', context)
    else:
        if profile.mail_is_verified == False:
            if profile.verification_mail_sent == False:
                profile.verification_mail_sent = True
                profile.send_verification_email()
                profile.save()
            return render(request, 'dashboard/profile_email_verify.html', context)
        else:
            return redirect('dashboard-home')


# Profile Page View of Application from this point onwards

@login_required
def ProfileMarkdown(request):
    profile = Profile.objects.get(user=request.user)
    context = {
        'website_name': website_name,
        'title': 'Profile - Public',
        'data': profile.bio
    }
    return render(request, 'dashboard/profile_publicpreview.html', context)


@login_required
def ProfileAbout(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = BioForm(request.POST)

        if form.is_valid():
            profile.bio = form.cleaned_data.get('bio')
            profile.save()
            context = {
                'website_name': website_name,
                'title': 'Profile - About',
                'bio_form': BioForm(initial={'bio': profile.bio}),
                'data': form.cleaned_data.get('bio')
            }
            return render(request, 'dashboard/profile_about.html', context)

    context = {
        'website_name': website_name,
        'title': 'Profile - About',
        'bio_form': BioForm(initial={'bio': profile.bio}),
        'data': profile.bio
    }
    return render(request, 'dashboard/profile_about.html', context)


@login_required
def ProfileEducation(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileEducationForm(request.POST)
        if form.is_valid():
            profile.degree_type = form.cleaned_data.get('degree_type')
            profile.grad_year = form.cleaned_data.get('grad_year')
            profile.field_of_study = form.cleaned_data.get('field_of_study')
            profile.institute = form.cleaned_data.get('institute')
            profile.course_length = form.cleaned_data.get('course_length')

            profile.save()
            context = {
                'website_name': website_name,
                'title': 'Profile - Education',
                'form': ProfileEducationForm(
                    initial={
                        'degree_type': profile.degree_type,
                        'grad_year': profile.grad_year,
                        'field_of_study': profile.field_of_study,
                        'institute': profile.institute,
                        'course_length': profile.course_length
                    }
                )

            }
            return render(request, 'dashboard/profile_edu.html', context)

    context = {
        'website_name': website_name,
        'title': 'Profile - Education',
        'form': ProfileEducationForm(
            initial={
                'degree_type': profile.degree_type,
                'grad_year': profile.grad_year,
                'field_of_study': profile.field_of_study,
                'institute': profile.institute,
                'course_length': profile.course_length
            }
        ),
    }
    return render(request, 'dashboard/profile_edu.html', context)


# Was planned to use but not being used right now
# class ProfileExperience(LoginRequiredMixin, UpdateView):
#     model = Profile
#     template_name = 'dashboard/profile_exp.html'
#     fields = ['skill']
#     form_class = ProfileExpForm

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['website_name'] = website_name
#         context['title'] = 'Profile - Experience'
#         context['form'] = ProfileExpForm,
#         context['form_work'] = ProfileWorkForm
#         context['work'] = Work.objects.filter(profile=profile),
#         return context


@login_required
def ProfileExperience(request):
    profile = Profile.objects.get(user=request.user)

    context = {
        'website_name': website_name,
        'title': 'Profile - Experience',
        'form': ProfileExpForm,
        'form_work': ProfileWorkForm,
        'works': Work.objects.filter(profile=profile),
        'skills': profile.skill.all()
    }

    return render(request, 'dashboard/profile_exp.html', context)


@login_required
def ProfileWorkCreate(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        form = ProfileWorkForm(request.POST)
        if form.is_valid():
            form.instance.profile = profile
            form.save()

    return redirect('profile-exp')


@login_required
def ProfileSkillConnect(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        form = ProfileExpForm(request.POST)
        print(form)
        if form.is_valid():
            skill = form.cleaned_data.get('skill')
            skill_add = Skill.objects.get(name=skill)
            profile.skill.add(skill_add)
            profile.save()

    return redirect('profile-exp')


@login_required
def ProfileExpResume(request):

    if request.method == 'POST':
        form = ProfileExpForm(request.POST,
                              request.FILES,
                              instance=request.user.profile)
        if form.is_valid():
            form.save()

    return redirect('profile-exp')


class InstituteAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Institute.objects.none()
        qs = Institute.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs


class SkillAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        if not self.request.user.is_authenticated:
            return Skill.objects.none()
        profile = Profile.objects.get(user=self.request.user)
        skills_discounted = profile.skill.all()
        qs = Skill.objects.all().order_by('name')
        qs = qs.exclude(id__in=[s.id for s in skills_discounted])
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs


class FieldofStudyAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return FieldofStudy.objects.none()
        qs = FieldofStudy.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs


class CityAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return City.objects.none()
        qs = City.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q,
                           state__istartswith=self.q)
        return qs


class SchoolAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return School.objects.none()
        qs = School.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs


@login_required
def ProfileLinks(request):
    context = {
        'website_name': website_name,
        'title': 'Profile - Links'
    }
    return render(request, 'dashboard/profile_links.html', context)


@login_required
def ProfileContact(request):
    context = {
        'website_name': website_name,
        'title': 'Profile - Links'
    }
    return render(request, 'dashboard/profile_contact.html', context)


@login_required
def settings(request):
    context = {
        'website_name': website_name,
        'title': 'Settings'
    }
    return render(request, 'dashboard/settings.html', context)


def profilepage(request):
    context = {
        'website_name': website_name,
        'title': 'Profile Page'
    }
    return render(request, 'unlogged/profile.html', context)
