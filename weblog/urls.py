from django.contrib import admin
from django.conf import settings
from django.urls import path , include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls',namespace='blog')),
    path('auth/',include('authentication_app.urls',namespace='authentication_app')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


