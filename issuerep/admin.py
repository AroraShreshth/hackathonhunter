# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import IssueType, Issue


@admin.register(IssueType)
class IssueTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_date', 'modified_date', 'name')
    list_filter = ('created_date', 'modified_date')
    search_fields = ('name',)


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'title',
        'detail',
        'posted_by',
        'is_type',
        'status',
        'response_comment',
    )
    list_filter = ('created_date', 'modified_date', 'posted_by', 'is_type')
