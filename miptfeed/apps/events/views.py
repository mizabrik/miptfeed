from datetime import datetime as dt, timedelta

from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from events.forms import CreateEventForm
from events.models import Event

from vk import Session, API
from vk.exceptions import VkAPIError

class EventListView(ListView):
    paginate_by = 20
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', 'give-default-value')
        order = self.request.GET.get('orderby', 'give-default-value')
        new_context = Event.objects \
                           .filter(date__gt=dt.now() - timedelta(hours=5),) \
                           .order_by('date')
        return new_context

class PersonalEventListView(LoginRequiredMixin, EventListView):
    def get_queryset(self):
        preferences = self.request.user.profile.preferences.all()
        print(preferences)
        return super(PersonalEventListView, self).get_queryset() \
                .filter(category__in=preferences)

class EventDetailView(DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        if 'group' in self.kwargs:
            context['group'] = self.kwargs['group']
        return context

class CreateEventView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = CreateEventForm

    def dispatch(self, request, *args, **kwargs):
        token = request.user.social_auth.get(provider='vk-oauth2').extra_data['access_token']
        api = API(Session(), access_token=token)
        groups = api.groups.get(filter='editor', extended=True, fields='is_closed')[1:]
        self.groups = [(None, '---------',)] + [(str(group['gid']), group['name'], ) for group in groups
                if group['is_closed'] < 2]

        return super(CreateEventView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateEventView, self).get_form_kwargs()
        kwargs['groups'] = self.groups
        return kwargs

    def get_success_url(self):
        return reverse('events:share-event', kwargs={'pk': self.object.pk,
            'group': self.group}, current_app='events') if self.group else \
            reverse('events:event-detail', kwargs={'pk': self.object.pk}, current_app='events')

    def form_valid(self, form):
        self.group = form.cleaned_data['group']

        return super(CreateEventView, self).form_valid(form)
