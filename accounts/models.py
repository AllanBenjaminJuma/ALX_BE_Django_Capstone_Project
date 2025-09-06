from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLES_CHOICES={
        ('client', 'Client'),
        ('architect', 'Architect'),
        ('admin', 'Admin'),
    }
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLES_CHOICES, default='client')
    phone_number = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return f"{self.username} ({self.role})"
    