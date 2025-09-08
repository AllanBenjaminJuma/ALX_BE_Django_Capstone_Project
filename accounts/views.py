from django.shortcuts import render
from rest_framework import generics, permissions, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

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

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'details': 'You successfully logged out.'}, status=status.HTTP_205_RESET_CONTENT)
        except KeyError:
            return Response({'error': 'refresh token required.'}, status=status.HTTP_400_BAD_REQUEST)
        except TokenError:
            return Response({'error': 'Invalid or expired token.'}, status=status.HTTP_400_BAD_REQUEST)