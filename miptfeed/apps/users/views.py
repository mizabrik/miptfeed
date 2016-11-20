from django.shortcuts import render
from django.views.generic import UpdateView
from django.urls import reverse

from users.models import Profile
from users.forms import UpdateForm


class MyUpdate(UpdateView):
    form_class = UpdateForm
    model = Profile

    def get_success_url(self):
        return reverse('users:profile', kwargs={'pk': self.object.pk}, current_app='users')
