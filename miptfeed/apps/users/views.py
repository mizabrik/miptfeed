from django.shortcuts import render
from django.views.generic import UpdateView
from django.urls import reverse
from categories.models import Category

from users.models import Profile
from users.forms import UpdateForm


class Update(UpdateView):
    form_class = UpdateForm
    model = Profile

    def get_success_url(self):
        return reverse('users:profile', kwargs={'pk': self.object.pk}, current_app='users')
    
    def get_context_data(self, **kwargs):
        context = super(Update, self).get_context_data(**kwargs)
        context["categories"] = []
        context["categories"] = Category.objects.all()
        return context

