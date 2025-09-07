from rest_framework import serializers
from .models import Architect, Projects

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'title', 'description', 'image', 'created_at']

class ArchitectSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    class Meta:
        model = Architect
        fields = ['id', 'user', 'bio', 'company', 'phone_number', 'specialization', 'years_of_experience', 'location', 'projects']