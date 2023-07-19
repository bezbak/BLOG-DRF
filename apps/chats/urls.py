from django.urls import path
from apps.chats.views import ChatAPIView, MessageAPIView
urlpatterns = [
    path('list/', ChatAPIView.as_view),
    path('messages_list/', MessageAPIView.as_view)
]
