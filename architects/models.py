from django.db import models
from django.conf import settings

# Create your models here.
# architect profiles
class Architect(models.Model):
    
    user = models.OneToOneField(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='architect_profile'
    )
    bio = models.TextField(blank=False)
    company = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=False, default= 0)
    specialization = models.CharField(max_length=255, blank=True)
    years_of_experience = models.PositiveBigIntegerField(default=0)
    location = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.user.username

# Projects added by an architect
class Projects(models.Model):
    architect = models.ForeignKey(
        Architect,
        on_delete=models.CASCADE,
        related_name='projects'
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
