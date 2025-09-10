from django.urls import path, include

from .views import (ArchitectListCreateView,ArchitectDetailView, ProjectListCreateView, ProjectDetailView, ArchitectProfileView)

urlpatterns = [
    path('', ArchitectListCreateView.as_view(), name='architect-list-create'),
    path('<int:pk>/', ArchitectDetailView.as_view(), name='architect-detail'),
    path('<int:architect_id>/projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('myprofile/', ArchitectProfileView.as_view(), name='architect-profile'),
    
]
