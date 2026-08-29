from django import forms
from django.forms import inlineformset_factory
from .models import Event, EventDate

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description']

class EventDateForm(forms.ModelForm):
    class Meta:
        model = EventDate
        fields = ['start_datetime', 'end_datetime']
        widgets = {
            'start_datetime': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
            'end_datetime': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
        }
    
EventDateFormSet = inlineformset_factory(Event, EventDate, form=EventDateForm, fields=('start_datetime', 'end_datetime'), extra=3, can_delete=True)

class VoteForm(forms.Form):
    dates = forms.ModelMultipleChoiceField(
        queryset=EventDate.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='Выберите удобные даты'
    )

    def __init__(self, *args, **kwargs):
        event = kwargs.pop('event')
        super().__init__(*args, **kwargs)
        self.fields['dates'].queryset = event.dates.all()
    


