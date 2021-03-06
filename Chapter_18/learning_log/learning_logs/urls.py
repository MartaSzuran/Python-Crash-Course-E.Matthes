"""Define url patterns for learning_logs."""

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    # particular page for each topic
    path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # path to page where user can add new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # path to add new entry to topic
    path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry')
]
