from rest_framework import generics, permissions
from django.shortcuts import render
from .models import Client
from .serializers import ClientSerializer

# Create your views here.
# for a logged in user to view or update their profile
class ClientProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    # to ensure that a client can only access his/her own profile
    def get_object(self):
        
        profile, created = Client.objects.get_or_create(user=self.request.user)
        
        return profile
