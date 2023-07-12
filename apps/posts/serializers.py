from rest_framework import serializers
from apps.posts.models import Post, Comment, Like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
    def create(self, validated_data):
        try:
            is_like = Like.objects.get(from_user = validated_data['from_user'], to_post = validated_data['to_post'])
            is_like.delete()
            return is_like
        except:
            is_like = Like.objects.create(from_user = validated_data['from_user'], to_post = validated_data['to_post'])
            is_like.save()
            return is_like

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
                
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    count_likes = serializers.SerializerMethodField()
    count_comments = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id', 'comments', 'image_or_video', 'description', 'created', 'user', 'count_likes', 'count_comments')
        
    def get_count_likes(self,obj):
        return f'{obj.liked_users.count()}'
    def get_count_comments(self,obj):
        return f"{obj.comments.count()}"
    
        
class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'image_or_video')
        
