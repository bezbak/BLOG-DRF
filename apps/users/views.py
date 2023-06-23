from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apps.users.models import User
from apps.users.serializers import UserSerializer, RegisterSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['posts']
    
class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer