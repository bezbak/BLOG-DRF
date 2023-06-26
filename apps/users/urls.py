from django.urls import path
from apps.users.views import RegisterAPIView, EmailCheckAPIView, ResetPasswordAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('check_email/', EmailCheckAPIView.as_view()),
    path('reset_password/', ResetPasswordAPIView.as_view()),
]
