from rest_framework import serializers
from apps.posts.models import Post

        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'image_or_video')