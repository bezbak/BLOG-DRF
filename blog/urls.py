from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

api_urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('posts/', include('apps.posts.urls')),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns))
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
