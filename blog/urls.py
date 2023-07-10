from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static
from rest_framework import routers
from apps.posts.views import PostViewSet, CommentViewSet
from apps.users.views import UsersViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UsersViewSet)
router.register(r'comments', CommentViewSet)

api_urlpatterns = [
    path('users/', include('apps.users.urls')),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
    path('api/', include(router.urls)),
    path('',RedirectView.as_view(url='/api/'))
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
