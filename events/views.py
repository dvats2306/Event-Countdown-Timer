from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm


def home(request):
    event = Event.objects.first()

    return render(request, 'events/home.html', {
        'event': event
    })


def add_event(request):

    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = EventForm()

    return render(request, 'events/add_event.html', {
        'form': form
    })