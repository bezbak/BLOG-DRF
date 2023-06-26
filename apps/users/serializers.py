from rest_framework import serializers
from django.core.mail import send_mail
from django.contrib.auth.password_validation import validate_password
from apps.users.models import User, EmailCheckCode
from apps.posts.serializers import UserPostSerializer
class UserSerializer(serializers.ModelSerializer):
    posts = UserPostSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'date_of_birth','profile_image','description','posts', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required = True, validators = [validate_password])
    confirm_password = serializers.CharField(write_only = True, required = True)
    class Meta:
        model = User
        fields = ('username','password', 'confirm_password' )
        
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password':"Пароли отличаются"})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class EmailCheck(serializers.ModelSerializer):
    email = serializers.CharField(write_only=True)
    code = serializers.CharField(read_only=True)
    class Meta:
        model = EmailCheckCode
        fields = ['email', 'code']
    
    def create(self, validated_data):
        if User.objects.filter(email=validated_data['email']).exists():
            user = User.objects.get(email = validated_data['email'])
            code = EmailCheckCode.objects.create(user=user, email=validated_data['email'])
            code.save()
            email_body = f"""
                Здравствуйте,
                вот ваш ферифиционный код {code.code}
            """
            send_mail(
                #subject 
                    f"Код подтверждения", 
                    #message 
                    email_body, 
                    #from email 
                    'noreply@somehost.local', 
                    #to email 
                    [user.email] 
            )
            return code
        
class ResetPasswordSerializer(serializers.ModelSerializer):
    code = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only = True, required = True, validators = [validate_password])
    confirm_password = serializers.CharField(write_only = True, required = True, validators = [validate_password])
    class Meta:
        model = User
        fields = ['code', 'password', 'confirm_password']