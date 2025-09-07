from .models import Architect, Projects
from .serializers import ArchitectSerializer, ProjectSerializer
from rest_framework import generics, permissions

# Create your views here.
class ArchitectListCreateView(generics.ListCreateAPIView):
    queryset = Architect.objects.all()
    serializer_class = ArchitectSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    # ensure that the logged in user is the one that creates the profile
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# 
class ArchitectDetailView(generics.RetrieveUpdateAPIView):
    queryset = Architect.objects.all()
    serializer_class = ArchitectSerializer
    permission_classes = [permissions.IsAuthenticated]

# list projects associated to a spcecific user who is currently logged in
class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Projects.objects.filter(architect__user = self.request.user)
    
    def perform_create(self, serializer):
        architect = Architect.objects.get(user = self.request.user)
        serializer.save(architect=Architect)
        
class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Projects.objects.filter(architect__user=self.request.user)