"""Define patterns for urls to application users."""

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    # login web
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    # logout web
    path('logout/', LogoutView.as_view(), name="logout"),
    # register  web
    path('register/', views.register, name='register'),
]
