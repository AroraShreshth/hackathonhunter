from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, SearchForm, NameForm, EmailVerifyForm
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
from users.models import Snippet, Profile
from django.contrib.auth import views as auth_views
from vacc.settings import website_name
from django.core.mail import send_mail


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
            messages.success(
                request, f'Your account has been created! You are now able to log in')
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


@login_required
def welcome(request):
    context = {
        'website_name': website_name,
        'title': 'Welcome',
        'name_form': NameForm
    }

    if request.method == 'POST':
        name_form = NameForm(request.POST, instance=request.user)

        if name_form.is_valid():
            name_form.save()
            messages.success(
                request, f'{request.user.username} Name Details Saved !')
            return render(request, 'dashboard/welcome.html', context)
    else:

        return render(request, 'dashboard/welcome.html', context)


class Welcome(LoginRequiredMixin, TemplateView):
    name_form = NameForm
    template_name = 'dashboard/welcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['website_name'] = website_name
        context['name_form'] = NameForm
        context['title'] = 'Welcome'
        return context


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

    context = {
        'website_name': website_name,
        'title': 'Verify Email',
        'form': EmailVerifyForm
    }

    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        ∂
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
                profile.save()
                messages.success(
                    request, f' Hey, {request.user.username} your email has been verfied successfully !')
                return redirect('dashboard-home')
            else:
                messages.error(
                    request, f' OOPS! {request.user.username} OTP provided is incorrect !')
                return render(request, 'dashboard/profile_email_verify.html', context)
    else:
        if profile.mail_is_verified == False:
            profile.send_verification_email()
            return render(request, 'dashboard/profile_email_verify.html', context)
        else:
            return redirect('dashboard-home')
