# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Quiz, Question, Option, Response


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'name',
        'subtitle',
        'user',
        'comp',
        'start_time',
        'end_time',
        'time_for_each_question',
        'timed_question',
    )
    list_filter = (
        'created_date',
        'modified_date',
        'user',
        'comp',
        'start_time',
        'end_time',
        'timed_question',
    )
    raw_id_fields = ('skills', 'participants')
    search_fields = ('name',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'quiz',
        'name',
        'types',
    )
    list_filter = ('created_date', 'modified_date', 'quiz')
    search_fields = ('name',)


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'question',
        'name',
    )
    list_filter = ('created_date', 'modified_date', 'question')
    search_fields = ('name',)


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'question',
        'user',
        'true_false',
    )
    list_filter = (
        'created_date',
        'modified_date',
        'question',
        'user',
        'true_false',
    )
    raw_id_fields = ('options',)
