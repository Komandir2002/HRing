from django.urls import path
from . import views


urlpatterns = [
    path("registr/", views.RegisterView.as_view(), name="registartion_view"),
    path("login/", views.NewLoginView.as_view(), name="login_view"),
    path("users/", views.UserListView.as_view(), name="user_listView"),
    path("employes/", views.Employes.as_view(), name="Employee"),
    path("employes/<int:id>/", views.EmployeDetailView.as_view(), name="Employee_Detail"),
    path(
        "employes/<int:id>/update/", views.EmployeUpdateView.as_view(), name="Employe_update"
    ),
    path(
        "employes/<int:id>/delete/", views.EmployeDeleteView.as_view(), name="Employe_delete"
    ),
    path("add_post/", views.EmployeCreatedateView.as_view(), name="Employe_add"),
]