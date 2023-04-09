from django.shortcuts import render
from django.views.generic import View , TemplateView , ListView , DeleteView , CreateView , UpdateView ,DetailView
from django.urls import reverse_lazy
from . import models

class HomePageView(TemplateView):
    template_name = 'home_page/home_page.html'

# =======================================================

class PostListView(ListView):
    model = models.Post
    template_name = 'blog_pages/post_list_page.html'
    context_object_name = 'posts'

# =======================================================

class PostDetailView(DetailView):
    model = models.Post
    context_object_name = 'post'
    template_name = 'blog_pages/post_detail_page.html'

# =======================================================

