from django.conf.urls import url

from events.views import CreateEventView, EventDetailView, EventListView

urlpatterns = [
    url(r'^$', EventListView.as_view(), name='event-list'),
    url(r'^(?P<pk>[0-9]+)/$', EventDetailView.as_view(), name='event-detail'),
    url(r'^create/$', CreateEventView.as_view(), name='create-event'),
]
