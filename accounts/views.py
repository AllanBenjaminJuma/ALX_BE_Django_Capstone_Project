from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer

# Create your views here.
# Register user as a client
class clientRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
    
    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['role'] = 'client'
        return ctx
# Register user as an arhictect
class ArchitectRegisterView(generics.CreateAPIView):
    
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
    
    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['role'] = 'architect'
        return ctx

class LoginView(TokenObtainPairView):
    
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

class ProfileView(generics.RetrieveAPIView):
    
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user