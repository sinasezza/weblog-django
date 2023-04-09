from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',view=views.HomePageView.as_view(),name='home_page'),
    path('Posts/',views.PostListView.as_view(),name='post_list'),
    path('Post/<int:pk>',views.PostDetailView.as_view(),name='post_detail'),


]