from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="listings-index"),
    path("<int:listing_id>", views.listing, name="listings-listing"),
    path("search/", views.search, name="listings-search"),
]
