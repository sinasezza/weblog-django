from django.urls import path
from . import views

app_name = 'authentication_app'

urlpatterns = [
    path('signup/',views.UserSignupView.as_view(),name='signup'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/<int:pk>/',views.UserLogoutView.as_view(),name='logout'),
    path('delete-account/<int:pk>/',views.UserDeleteView.as_view(),name='delete-account'),
    path('profile/<int:pk>-<str:username>/',views.UserProfileView.as_view(),name='user-profile'),
    path('change-profile/<int:pk>/',views.UserChangeProfileView.as_view(),name='user-change-profile'),
    path('panel/me',views.UserPanelView.as_view(),name='user-panel'),
]

