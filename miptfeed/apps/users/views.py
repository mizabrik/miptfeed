from django.shortcuts import render
from django import forms
from .forms import UpdateForm
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from users.models import Profile


class MyUpdate(UpdateView):
    form_class = UpdateForm
    model = Profile
            
    
    