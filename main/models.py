from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    

class EventDate(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCASE, related_name="dates")
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    votes_count = models.PositiveIntegerField(default=0)
    
    
class Vote(models.Model):
    event_date = models.ForeignKey(EventDate, on_delete=models.CASCASE, related_name="votes")
    voter_name = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    

