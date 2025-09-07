from django.db import models
from django.conf import settings


# Create your models here.
class Client(models.Model):
    user  =models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='client_profile'
    )
    phone_number = models.CharField(max_length=20, blank=False, default= '0')
    location = models.CharField(max_length=255, blank = False, default="Nairobi")
    preferences = models.TextField(blank=True, null=True, help_text="e.g Residential, Commercial")
    profile_image = models.ImageField(upload_to='client_profiles', blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Client Profile of {self.user.username}"
