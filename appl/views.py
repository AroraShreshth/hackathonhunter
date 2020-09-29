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
from comp.models import Event

# Competiton Dashboard Panel


class CompListView(LoginRequiredMixin, ListView):
    template_name = 'appl/comp.html'
    model = Event
    context_obj_name = 'event.html'
    ordering = ['-created_date']
    paginate_by = 20
