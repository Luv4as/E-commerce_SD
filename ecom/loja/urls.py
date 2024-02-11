from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/sobre_nos', views.about, name='sobre_nos'),
]
