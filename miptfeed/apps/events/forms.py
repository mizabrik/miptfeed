from django.forms import ModelForm, ChoiceField

from events.models import Event

class CreateEventForm(ModelForm):
    def __init__(self, groups, *args, **kwargs):
        super(CreateEventForm, self).__init__(*args, **kwargs)
        self.fields['group'] = ChoiceField(choices=groups)

    """
    Форма изменения UID пропуска.
    """
    class Meta:
        model = Event
        fields = ('title', 'date', 'place', 'description',)

    def clean_pass_id(self):
        data = self.cleaned_data['pass_id']
        return data.lower().replace(' ', '')
