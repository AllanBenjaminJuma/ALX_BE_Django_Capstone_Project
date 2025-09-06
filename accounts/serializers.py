from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Display user details to clients
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'phone_number','first_name', 'last_name', 'date_joined']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length = 8)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role', 'phone_number', 'first_name', 'last_name']
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        role = self.context.get('role', 'client') # default to client if role is not provided
        
        user = User(**validated_data)
        user.role = role
        user.set_password(password) # hashes the set password
        user.save()
        return user

# log in the user
    
class LoginSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role
        token['username'] = user.username
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = {
            'id':self.user.id,
            'username':self.user.username,
            'role':self.user.role,
            'email':self.user.email,
        }
        return data