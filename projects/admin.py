# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Project, ProjectLink, ProjectPhotos, ProjectFiles, Discuss


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'name',
        'subtitle',
        'description',
        'challenges',
        'slug',
        'event',
        'published',
        'public',
        'under_review',
        'official',
        'winner',
        'views',
    )
    list_filter = (
        'created_date',
        'modified_date',
        'event',
        'published',
        'public',
        'under_review',
        'official',
        'winner',
    )
    raw_id_fields = ('users', 'skills', 'likes')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}


@admin.register(ProjectLink)
class ProjectLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_date', 'modified_date', 'project', 'url')
    list_filter = ('created_date', 'modified_date', 'project')


@admin.register(ProjectPhotos)
class ProjectPhotosAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'project',
        'image',
    )
    list_filter = ('created_date', 'modified_date', 'project')


@admin.register(ProjectFiles)
class ProjectFilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_date', 'modified_date', 'project', 'file')
    list_filter = ('created_date', 'modified_date', 'project')


@admin.register(Discuss)
class DiscussAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_date', 'modified_date', 'user', 'content')
    list_filter = ('created_date', 'modified_date', 'user')
    raw_id_fields = ('likes',)
