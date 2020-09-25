# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Institute, FieldofStudy, Skill, Profile, Work, Link, Snippet

admin.site.register(Snippet)


@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_date', 'modified_date', 'name')
    list_filter = ('created_date', 'modified_date')
    search_fields = ('name',)


@admin.register(FieldofStudy)
class FieldofStudyAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_date', 'modified_date', 'name')
    list_filter = ('created_date', 'modified_date')
    search_fields = ('name',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_date', 'modified_date', 'name')
    list_filter = ('created_date', 'modified_date')
    search_fields = ('name',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'mail_is_verified',
        'phone_is_verified',
        'published',
        'image',
        'bio',
        'shirt_size',
        'no_formal_education',
        'degree_type',
        'institute',
        'field_of_study',
        'grad_year',
        'skill',
        'resume',
        'work_status',
        'phone',
        'address',
        'emergency_contact_name',
        'emergency_phone',
    )
    list_filter = (
        'created_date',
        'modified_date',
        'published',
        'no_formal_education',
        'institute',
        'field_of_study',
        'grad_year',
        'skill',
        'work_status',
    )
    readonly_fields = ('phone_otp', 'mail_otp', 'created_date',
                       'modified_date')


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'profile',
        'employer',
        'role',
        'start',
        'end',
        'currently_working',
        'description',
        'url',
    )
    list_filter = (
        'created_date',
        'modified_date',
        'profile',
        'start',
        'end',
        'currently_working',
    )


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_date', 'modified_date', 'profile', 'url')
    list_filter = ('created_date', 'modified_date', 'profile')
