from django.urls import path
from . import views


urlpatterns = [
    path("", views.main, name="main_page"),
    path("home/", views.home, name="home_page"),
]