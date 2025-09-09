from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Client
        fields = ['id', 'user', 'phone_number', 'preferences', 'location','created_at']
        read_only_fields = ['id', 'user', 'created_at']