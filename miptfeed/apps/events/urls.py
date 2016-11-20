from django.conf.urls import url

from events.views import CreateEventView, EventDetailView, EventListView, PersonalEventListView

urlpatterns = [
    url(r'^$', EventListView.as_view(), name='event-list'),
    url(r'^my/$', PersonalEventListView.as_view(), name='personal-event-list'),
    url(r'^(?P<pk>[0-9]+)/$', EventDetailView.as_view(), name='event-detail'),
    url(r'^(?P<pk>[0-9]+)/share/(?P<group>[0-9]+)/$', EventDetailView.as_view(), name='event-detail'),
    url(r'^(?P<pk>[0-9]+)/share/(?P<group>[0-9]+)/$', EventDetailView.as_view(), name='share-event'),
    url(r'^create/$', CreateEventView.as_view(), name='create-event'),
]
