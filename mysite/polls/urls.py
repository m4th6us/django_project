from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/details", views.details, name="details"),
    path("<int:question_id>/results", views.results, name="results"),
    path("<int:question_id>/votes", views.votes, name="votes")
]