"""Define url patterns for blogs."""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('new_post', views.new_post, name='new_post'),
    path(r'^edit_post/(?P<post_id>\d+)/$', views.edit_post, name='edit_post'),
]
