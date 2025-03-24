from django.urls import path

from .views import AdminAPIs, StudentAPI

urlpatterns = [
    path("admin/", AdminAPIs.as_view(), name="list-create"),
    path("admin/<int:pk>/", AdminAPIs.as_view(), name="get-update-delete"),
    path("nt/", StudentAPI.as_view(), name="student-books-listview"),
]
