# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Institute, FieldofStudy, Skill, School, City, Profile, Work, Link, Snippet, SchoolEducation


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


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_date', 'modified_date', 'name')
    list_filter = ('created_date', 'modified_date')
    search_fields = ('name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_date', 'modified_date', 'name', 'state')
    list_filter = ('created_date', 'modified_date')
    search_fields = ('name',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'user',
        'mail_is_verified',
        'phone_is_verified',
        'verification_mail_sent',
        'published',
        'setup',
        'image',
        'bio',
        'dob',
        'mail_otp',
        'phone_otp',
        'shirt_size',
        'gender',
        'no_formal_education',
        'completed_school',
        'degree_type',
        'institute',
        'field_of_study',
        'grad_year',
        'course_length',
        'resume',
        'work_status',
        'phone',
        'address',
        'location',
        'emergency_contact_name',
        'emergency_phone',
    )
    list_filter = (
        'created_date',
        'modified_date',
        'user',
        'mail_is_verified',
        'phone_is_verified',
        'verification_mail_sent',
        'published',
        'setup',
        'dob',
        'no_formal_education',
        'completed_school',
        'institute',
        'field_of_study',
        'grad_year',
        'work_status',
        'location',
    )
    search_fields = ('user', )
    raw_id_fields = ('skill',)


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


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_date', 'modified_date', 'title', 'body')
    list_filter = ('created_date', 'modified_date')


@admin.register(SchoolEducation)
class SchoolEducationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'profile',
        'school',
        'from_standard',
        'to_standard',
    )
    autocomplete_fields = ['profile', 'school']
    search_fields = ('profile', 'school', )
