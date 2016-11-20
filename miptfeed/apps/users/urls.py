from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from users.views import Update

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
#    url(r'^profile/$', login, {'template_name': 'users/profile.html'}, name='profile'),
    url(r'^profile/(?P<pk>[0-9]+)/$', Update.as_view(), name='profile'),

    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url('', include('social.apps.django_app.urls', namespace='social')),
]
