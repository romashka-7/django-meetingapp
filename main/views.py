from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, EventDate, Vote
from .forms import EventForm, EventDateFormSet, VoteForm
from django.contrib import messages

def event_list(request):
    events = Event.objects.all().order_by('-created_at')
    
    return render(request, 'main/event/event_list.html', {'events': events,})
    

def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        formset = EventDateFormSet(request.POST)
        if form.is_valid and formset.is_valid():
            event = form.save()
            formset.instance = event
            formset.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm()
        formset = EventDateFormSet()
    return render(request, 'main/event/event_form.html', {
        'form': form,
        'formset': formset,
    })
    
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    dates = event.dates.all()
    if request.method == "POST":
        form = VoteForm(request.POST, event=event)
        if form.is_valid():
            selected_dates = form.cleaned_data['dates']
            for date in selected_dates:
                Vote.objects.create(event_date=date)
            messages.success(request, 'Ваш голос учтён!')
            return redirect('main:event_detail', pk=event.pk)
    else:
        form = VoteForm(event=event)
    return render(request, 'main/event/event_detail.html', 
                  {'event': event,
                   'dates': dates,
                   'form': form,})