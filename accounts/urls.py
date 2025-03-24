from django.urls import path

from .views import RegisterAPI, LoginAPI

urlpatterns = [
    path("register/nt/", RegisterAPI.as_view()),
    path("login/nt/", LoginAPI.as_view()),
]
