from django.shortcuts import get_object_or_404
from rest_framework import permissions
from django.contrib.auth.models import User
from users.models import Snippet, City, Institute, FieldofStudy, Skill, School, Profile, Work, Link, SchoolEducation


class Authenticated(permissions.IsAuthenticated):
    pass
