# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Location, Event, Announcement, ApplicationQuestion, TimelineEvent, Judge, FAQ, SponsorType, Sponsor, PrizeType, Prize, EventMember, Feedback


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'city',
        'state',
        'country',
    )
    list_filter = ('created_date', 'modified_date')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'name',
        'tagline',
        'description',
        'slug',
        'start_date',
        'end_date',
        'is_online',
        'published',
        'verified',
        'official',
        'is_team_comp',
        'image',
        'cover_image',
        'Location',
        'address',
        'longitute',
        'latitute',
        'women_only',
        'approx_particpants',
        'team_size',
        'team_min',
        'winner_announced',
        'rsvp_email_sent_at',
        'reminder_email_sent_at',
        'feedback_reminder_sent_at',
        'not_accepeted_message',
        'waitlist_message',
        'accepted_message',
        'website',
        'twitter',
        'facebook',
        'linkedin',
        'medium',
        'instagram',
        'coc',
        'organiser_admin',
    )
    list_filter = (
        'created_date',
        'modified_date',
        'start_date',
        'end_date',
        'is_online',
        'published',
        'verified',
        'official',
        'is_team_comp',
        'Location',
        'women_only',
        'winner_announced',
        'rsvp_email_sent_at',
        'reminder_email_sent_at',
        'feedback_reminder_sent_at',
        'organiser_admin',
    )
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'event',
        'content',
    )
    list_filter = ('created_date', 'modified_date', 'event')


@admin.register(ApplicationQuestion)
class ApplicationQuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'required',
        'types',
        'event',
        'question',
    )
    list_filter = ('created_date', 'modified_date', 'required', 'event')


@admin.register(TimelineEvent)
class TimelineEventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'event',
        'important',
        'date',
        'name',
        'description',
    )
    list_filter = (
        'created_date',
        'modified_date',
        'event',
        'important',
        'date',
    )
    search_fields = ('name',)


@admin.register(Judge)
class JudgeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'event',
        'user',
        'only_speaker',
        'name',
        'position',
        'company',
        'link',
        'detail',
        'image',
    )
    list_filter = (
        'created_date',
        'modified_date',
        'event',
        'user',
        'only_speaker',
    )
    search_fields = ('name',)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'event',
        'question',
        'answer',
    )
    list_filter = ('created_date', 'modified_date', 'event')


@admin.register(SponsorType)
class SponsorTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'event',
        'priority',
        'size',
        'name',
    )
    list_filter = ('created_date', 'modified_date', 'event')
    search_fields = ('name',)


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'type',
        'name',
        'detail',
        'image',
    )
    list_filter = ('created_date', 'modified_date', 'type')
    search_fields = ('name',)


@admin.register(PrizeType)
class PrizeTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'event',
        'priority',
        'size',
        'name',
    )
    list_filter = ('created_date', 'modified_date', 'event')
    search_fields = ('name',)


@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'type',
        'name',
        'value',
        'awarded_to',
    )
    list_filter = ('created_date', 'modified_date', 'type', 'awarded_to')
    search_fields = ('name',)


@admin.register(EventMember)
class EventMemberAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'user',
        'event',
        'roll_name',
        'public',
        'overview',
        'review',
        'volunteer',
        'admin',
        'feedback',
    )
    list_filter = (
        'created_date',
        'modified_date',
        'user',
        'event',
        'public',
        'overview',
        'review',
        'volunteer',
        'admin',
        'feedback',
    )


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_date',
        'modified_date',
        'event',
        'question',
    )
    list_filter = ('created_date', 'modified_date', 'event')
