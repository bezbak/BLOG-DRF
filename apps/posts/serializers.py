from rest_framework import serializers
from apps.posts.models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
                
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = '__all__'
        
class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'image_or_video')
        
