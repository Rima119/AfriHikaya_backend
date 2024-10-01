from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
class CreateCustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'first_name', 'last_name', 'country', 'native_language', 'hobbies', 'profile_pic_url', 'roles']

class ReturnedUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'first_name', 'last_name', 'country', 'native_language', 'hobbies', 'profile_pic_url', 'roles']

class UpdateCustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'first_name', 'last_name', 'country', 'native_language', 'hobbies', 'profile_pic_url', 'roles']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['user_id'] = user.id
        token['username'] = user.username
        token['email'] = user.email
        token['roles'] = user.roles
        
        return token