"""Define URL patterns for application uesrs."""

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    # login website
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    # logout website
    path('logout/', LogoutView.as_view(), name="logout"),
    # registration website
    path('register/', views.register, name='register'),

]
