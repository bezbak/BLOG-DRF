from django.urls import path
from apps.users.views import UsersAPIView, RegisterAPIView, UserAPIView, UserUpdateAPIView

urlpatterns = [
    path('', UsersAPIView.as_view()),
    path('<int:pk>/', UserAPIView.as_view()),
    path('update/<int:pk>/', UserUpdateAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
]
