from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',view=views.HomePageView.as_view(),name='home-page'),
    path('Posts/',views.PostListView.as_view(),name='post-list'),
    path('Post/<int:pk>',views.PostDetailView.as_view(),name='post-detail'),


]