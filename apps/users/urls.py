from django.urls import path
from apps.users.views import UsersAPIView, RegisterAPIView, UserAPIView

urlpatterns = [
    path('', UsersAPIView.as_view()),
    path('<int:pk>/', UserAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
]
