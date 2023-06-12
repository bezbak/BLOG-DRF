from django.contrib import admin
from django.urls import path, include

api_urlpatterns = [
    path('users/', include('apps.users.urls'))
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns))
]
