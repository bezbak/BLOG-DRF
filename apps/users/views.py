from rest_framework import generics
from apps.users.models import User
from apps.users.serializers import UserSerializer, RegisterSerializer

class UsersAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class UserAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer   
    
class UserDestroyAPIVIew(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 