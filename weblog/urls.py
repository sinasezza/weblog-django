from django.contrib import admin
from django.conf import settings
from django.urls import path , include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls',namespace='blog')),
    path('auth/',include('authentication_app.urls',namespace='authentication_app')),
    path("__reload__/", include("django_browser_reload.urls")),
] 


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)