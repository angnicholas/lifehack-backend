from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model() #Retrieve custom user model

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = '__all__'
        fields = ('id', 'email', 'display_name', 'password', 'role', 'created_at')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'display_name', 'role')

        

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        ## This data variable will contain refresh and access tokens
        data = super().validate(attrs)
        print('hit')
        ## You can add more User model's attributes like username,email etc. in the data dictionary like this.
        data['role'] = self.user.role
        data['id'] = self.user.pk
        return data

