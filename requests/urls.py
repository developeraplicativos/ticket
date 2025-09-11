from django.urls import path
from . import views

urlpatterns = [
    path("", views.visualizar, name="visualizar"),
]