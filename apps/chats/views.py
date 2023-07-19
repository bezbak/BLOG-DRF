from rest_framework import generics, viewsets
from apps.chats.models import Chat, Message
from apps.chats.serializers import ChatCreateSerializer, ChatViewSerializer, MessageCreateSerializer, MessageViewSerializer

class ChatAPIView(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatViewSerializer
    
class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatCreateSerializer
    
class MessageAPIView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageViewSerializer
    
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageCreateSerializer