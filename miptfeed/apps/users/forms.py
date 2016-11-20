from django import forms;
from django.forms import ModelForm
from django.contrib.auth.models import User
from categories.models import Category
from users.models import Profile

class UpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['preferences']
        widgets = {
            #'preferences': forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple ,required=True,
         #                                                 queryset=Category.objects.all())
             'preferences': forms.CheckboxSelectMultiple,
        }
