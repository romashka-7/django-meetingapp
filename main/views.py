from django.shortcuts import render



def event_list(request):
    event = get_object_or_404(Event)
    options = event.
    
