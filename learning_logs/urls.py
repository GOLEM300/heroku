"""set url schema for learning_logs"""

from django.conf.urls import url

from . import views

app_name= 'learning_logs'

urlpatterns = [
    #home page
    url(r'^$', views.index, name='index'),

    #all pages
    url(r'^topics/$', views.topics, name='topics'),

    #one page
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name = 'topic'),

    #page for adding new page 
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    #page for add new_entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    #page edit
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]