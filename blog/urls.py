#Django Urls

from urllib import request
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .views import HomeView, BlogDetailView, delete_post, login_request, register_request, logout_request, publishBlog, delete_post

# Urls for the blog app, / is the home page it is using the home view from the views.py file

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("article/<slug:slug>/", BlogDetailView.as_view(), name="blog_detail"),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("post", publishBlog, name="post"),
    path("logout", logout_request, name= "logout"),
    path('articles/<slug:slug>/delete/', delete_post, name='delete_blog'),
    ]

