from django.forms import ModelForm

from events.models import Event

class CreateEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date']
