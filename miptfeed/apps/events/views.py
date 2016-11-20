from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse

from events.models import Event

class EventListView(ListView):
    model = Event

class EventDetailView(DetailView):
    model = Event

class CreateEventView(CreateView):
    model = Event
    fields = ['title', 'date', 'place', 'description']

    def get_success_url(self):
        return reverse('events:event-detail', kwargs={'pk': self.object.pk}, current_app='events')
