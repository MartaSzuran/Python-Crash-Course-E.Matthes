from django.urls import path

from . import views

urlpatterns = [
    path('home_page/', views.home_page, name='home_page'),
    path('pizzas/', views.pizzas, name='pizzas'),
    path(r'^pizzas/(?P<pizza_id>\d+)/$', views.pizza, name='pizza')
]
