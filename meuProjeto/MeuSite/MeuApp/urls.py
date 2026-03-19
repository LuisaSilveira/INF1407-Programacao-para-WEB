from django.urls import path
from MeuApp import views

urlpatterns = [
    path("", views.home, name="home"),
]