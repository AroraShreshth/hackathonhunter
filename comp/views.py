from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from users.models import Snippet, Profile
from vacc.settings import website_name
from .models import Event


# Competiton Organisation Panel


class Start(LoginRequiredMixin, TemplateView):
    template_name = 'comp/start.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['website_name'] = website_name
        context['title'] = 'About'
        return context


class Pricing(TemplateView):
    template_name = 'comp/pricing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['website_name'] = website_name
        context['title'] = 'Pricing'
        return context
