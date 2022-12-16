from django.urls import path
from . import views


urlpatterns = [
    path("staffing/", views.Staffing_table.as_view(), name="staffing_list"),
    path("add_staffing/", views.StaffingCreatedateView.as_view(), name="staffing_add"),
]