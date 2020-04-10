from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="pages-index"),
    path("about/", views.about, name="pages-about"),
]
