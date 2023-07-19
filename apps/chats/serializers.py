from rest_framework import serializers
from apps.chats.models import Chat, Message
from apps.users.serializers import ChatUserSerializer

class ChatViewSerializer(serializers.ModelSerializer):
    user_one = ChatUserSerializer(read_only=True)
    user_two = ChatUserSerializer(read_only=True)
    class Meta:
        model = Chat
        fields = "__all__"
        
class ChatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"
        
class MessageViewSerializer(serializers.ModelSerializer):
    from_user = ChatUserSerializer(read_only=True)
    to_user = ChatUserSerializer(read_only=True)
    class Meta:
        model = Message
        fields = "__all__"

class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"