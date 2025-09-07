from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Client

User = settings.AUTH_USER_MODEL
# create a client profile as soon as a client registers

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_client_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'client':
        Client.objects.create(user=instance)
        