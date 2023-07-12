from rest_framework import viewsets
from apps.posts.models import Post, Comment, Like
from apps.posts.serializers import PostSerializer, CommentSerializer, LikeSerializer
# Create your views here.

class PostViewSet(viewsets.ModelViewSet): 
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    