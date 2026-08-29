from django import forms
from django.forms import formset_factory
from .models import EventDate

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description']
    
    
EventDateFormSet = inlineformset_factory(Event, EventDate, fields=('start_datetime', 'end_datetime'), extra=3, can_delete=True)

class VoteForm(forms.Form):
    checkboxs = forms.MultipleChoiceField()
    
    


