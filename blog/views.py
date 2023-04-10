from django.shortcuts import render
from django.views.generic import View , TemplateView , ListView , DeleteView , CreateView , UpdateView ,DetailView
from django.urls import reverse_lazy
from . import models

class HomePageView(TemplateView):
    template_name = 'home_page/home_page.html'

# =======================================================

class PostListView(ListView):
    template_name = 'blog_pages/post_list_page.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        published_post      = models.Post.objects.filter(post_status='published')
        return published_post 
    

# =======================================================

class PostDetailView(DetailView):
    model = models.Post
    context_object_name = 'post'
    template_name = 'blog_pages/post_detail_page.html'
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        post_images = models.PostImage.objects.filter(post_id__exact = context['post'].id)
        context['post_images'] = post_images
        return context

# =======================================================

