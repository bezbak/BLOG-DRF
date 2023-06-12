from django.urls import path
from apps.users.views import UserAPIView

urlpatterns = [
    path('', UserAPIView.as_view()),
]
