from django.forms import ModelForm, ChoiceField
from datetimewidget.widgets import DateTimeWidget
from datetimewidget.widgets import DateWidget

from events.models import Event

class CreateEventForm(ModelForm):
    def __init__(self, groups, *args, **kwargs):
        super(CreateEventForm, self).__init__(*args, **kwargs)
        self.fields['group'] = ChoiceField(choices=groups, required=False)

    """
    Форма изменения UID пропуска.
    """
    class Meta:
        model = Event
        fields = ('title', 'date', 'place', 'description', 'category',)
        widgets = {
            'date': DateTimeWidget(usel10n = True, bootstrap_version=3)
        }


    def clean_pass_id(self):
        data = self.cleaned_data['pass_id']
        return data.lower().replace(' ', '')
