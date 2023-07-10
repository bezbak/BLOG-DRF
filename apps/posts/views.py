from rest_framework import viewsets
from apps.posts.models import Post, Comment
from apps.posts.serializers import PostSerializer, CommentSerializer
# Create your views here.

class PostViewSet(viewsets.ModelViewSet): 
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    