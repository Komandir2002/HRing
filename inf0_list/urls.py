from django.urls import path
from . import views


urlpatterns = [
    path("info_list/", views.Info_list_all.as_view(), name="info_list"),
    path("add_info/", views.Info_listCreatedateView.as_view(), name="info_list_add"),
]