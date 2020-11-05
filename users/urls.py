"""url for users"""

from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

app_name= 'users'

urlpatterns = [
    #entry page
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),

    #logout link
    url(r'^logout/$', views.logout_view, name='logout'),

    #reg page
    url(r'^register/$', views.register, name='register'),
]