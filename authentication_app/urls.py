from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name = 'authentication_app'

urlpatterns = [
    path('signup/', views.UserSignupView.as_view(), name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('delete-account/', views.UserDeleteView.as_view(), name='delete-account'),
    path('profile/@<str:username>/', views.UserProfileView.as_view(), name='user-profile'),
    path('change-profile/@<str:username>/', views.UserChangeProfileView.as_view(), name='user-change-profile'),
    path('panel/me', views.UserPanelView.as_view(), name='user-panel'),
]

