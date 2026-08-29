from django.contrib import admin
from .models import Event, EventDate, Vote

@admin.register(Event)
@admin.register(EventDate)
@admin.register(Vote)
