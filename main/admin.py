from django.contrib import admin
from .models import Event, EventDate, Vote

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at']


@admin.register(EventDate)
class EventDateAdmin(admin.ModelAdmin):
    list_display = ['event', 'start_datetime', 'end_datetime']
    list_filter = ('event',)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['event_date', 'voter_name', 'created_at']
    list_filter = ('event_date',)
