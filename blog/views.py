from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView

# Create your views here.

# Home view for blog
class HomeView(ListView):
    model = Blog
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'