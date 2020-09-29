from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import (UserRegisterForm, UserUpdateForm, ProfileUpdateForm,
                    SearchForm, NameForm, EmailVerifyForm, ProfileAboutForm, UserLoginForm)
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
from vacc.settings import website_name
from .models import Issue, IssueType


class IssueList(LoginRequiredMixin, ListView):
    model = Issue
    template_name = 'issuerep/main.html'
    context_object_name = 'issues'
    ordering = ['-created_date']
    paginate_by = 20


class YourIssues(LoginRequiredMixin, ListView):
    model = Issue
    template_name = 'issuerep/yourlist.html'
    context_object_name = 'issues'
    ordering = ['-created_date']
    paginate_by = 20


class CreateIssue(LoginRequiredMixin, CreateView):
    model = Issue
    template_name = 'issuerep/create.html'
    fields = ['is_type', 'title', 'detail']

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)
