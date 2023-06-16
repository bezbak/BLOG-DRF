from django.urls import path
from apps.users.views import UsersAPIView, RegisterAPIView, UserAPIView, UserUpdateAPIView, UserDestroyAPIVIew

urlpatterns = [
    path('', UsersAPIView.as_view()),
    path('<int:pk>/', UserAPIView.as_view()),
    path('update/<int:pk>/', UserUpdateAPIView.as_view()),
    path('delete/<int:pk>/', UserDestroyAPIVIew.as_view()),
    path('register/', RegisterAPIView.as_view()),
]
