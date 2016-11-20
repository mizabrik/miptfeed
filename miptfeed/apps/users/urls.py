from django.conf.urls import url, include
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url('', include('social.apps.django_app.urls', namespace='social')),
]
