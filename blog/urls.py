#Django Urls

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .views import HomeView, BlogDetailView

# Urls for the blog app, / is the home page it is using the home view from the views.py file

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("article/<slug:slug>/", BlogDetailView.as_view(), name="blog_detail"),
    ]

