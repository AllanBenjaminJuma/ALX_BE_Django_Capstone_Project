from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingsReadSerializer, BookingCreateSerializer
from  .permissions import IsClient, IsBookingParticipatOrAdmin, IsArchitect
from client.models import Client
from architects.models import Architect

# Create your views here.
class ClientBookingListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsClient]
    
    def get_serializer_class(self):
        return BookingsReadSerializer if self.request.method == 'GET' else BookingCreateSerializer
    
    def get_queryset(self):
        client_profile = Client.objects.get(user=self.request.user)
        return Booking.objects.filter(client=client_profile)
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
        architect_id = self.request.data.get('architect_id')
        if not architect_id:
            raise serializers.ValidationError({'architect_id': 'This field is required.'})
        try:
            architect = Architect.objects.get(pk=architect_id)
        except Architect.DoesNotExist:
            raise serializers.ValidationError({'architect_id': 'Invalid architect'})
        
        serializer = self.get_serializer(data=self.request.data, context={'architect': architect})
        serializer = is_valid(raise_exception=True)
        serializer.save(client=client_profile, architect=architect)

class BookingDetailView(generics.RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingsReadSerializer
    permission_classes = [permissions.IsAuthenticated, IsBookingParticipatOrAdmin]
    
    # specify the fields that client and architecture can edit
    def patch(self, request, *args, **kwargs):
        booking = self.get_object()
        
        user = request.user
        if hasattr(user, 'client_profile') and booking.client.user_id == user.id:
            serializer = BookingCreateSerializer(booking, data = request.data, partial=True, context={'architect':booking.architect})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(BookingsReadSerializer(booking).data)
        
        if hasattr(user, 'architect_profile') and booking.architect.user_id == user.id:
            status_value = request.data.get('status')
            if status_value not in dict(Booking.STATUS_CHOICES):
                return Response(BookingsReadSerializer(booking).data)
        return Response({'detai': 'Not allowed'}, status=status.HTTP_403_FORBIDDEN)
    
class ArchitectBookingListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsArchitect]
    serializer_class   =BookingsReadSerializer
    serializer_class = BookingsReadSerializer
    
    def get_queryset(self):
        architect_profile = Architect.objects.get(user=self.request.user)
        return Booking.objects.filter(architect=architect_profile)