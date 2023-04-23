from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',view=views.HomePageView.as_view(),name='home-page'),
    path('Posts/',views.PostListView.as_view(),name='post-list'),
    path('Post/<int:pk>-<str:slug>/',views.PostCombine_detail_comment_View.as_view(),name='post-detail'),
    path('post-create/',views.PostCreateView.as_view(),name='post-create'),
    path('post-update/<int:pk>-<str:slug>/',views.PostUpdateView.as_view(),name='post-update'),
    path('post-status-update/<int:pk>-<str:slug>/',views.PostStatusUpdateView.as_view(),name='post-status-update'),
    path('post-delete/<int:pk>/',views.PostDeleteView.as_view(),name='post-delete'),
    path('post-comment-create/<int:pk>',views.PostCommentCreateView.as_view(),name='post-comment-create'),
    

]