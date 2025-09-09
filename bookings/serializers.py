from rest_framework import serializers
from .models import Booking
from django.utils import timezone
from architects.serializers import ProjectSerializer
from client.serializers import ClientSerializer
from architects.serializers import ArchitectSerializer

class BookingsReadSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    architect = ArchitectSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)
    
    class Meta:
        model = Booking
        fields=[
            'architect_id', 'client', 'architect',
            'appointment_date', 'status', 'notes',
            'attachment', 'created_at', 'updated_at'
        ]
class BookingCreateSerializer(serializers.ModelSerializer):
    architect_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Booking
        fields = ['architect_id', 'appointment_date', 'notes']
       
        
     # ensure that the date of the appointment is in future   
    def validate_appointment_date(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError('The date must be in  the future.')
        return value
    # prevent booking the same architect at the same time
    def validate(self, data):
        architect = self.context.get('architect')
        appointment_date = data.get('appointment_date')
        if Booking.objects.filter(architect = architect, appointment_date=appointment_date, status__in=[Booking.STATUS_PENDING, Booking.STATUS_CONFIRMED]).exists():
            raise serializers.ValidationError("Architect already has a booking at this time.")
        
        return data