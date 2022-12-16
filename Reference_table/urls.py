from django.urls import path
from . import views


urlpatterns = [
    path("referense/", views.Reference_table_view.as_view(), name="reference_table_view"),
    path("referense/<int:id>/", views.ReferenceDetailView.as_view(), name="Reference_Detail"),
    path(
        "referense/<int:id>/update/", views.ReferenceUpdateView.as_view(), name="Reference_update"
    ),
    path(
        "referense/<int:id>/delete/", views.ReferenceDeleteView.as_view(), name="Reference_delete"
    ),
    path("add_reference/", views.ReferenceCreatedateView.as_view(), name="Reference_add"),
]