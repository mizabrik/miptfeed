from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from events.models import Event
from events.forms import CreateEventForm

class EventListView(ListView):
    model = Event

class EventDetailView(DetailView):
    model = Event

class CreateEventView(CreateView):
    form_class = CreateEventForm
