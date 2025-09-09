from django.db import models
from django.conf import settings
# Create your models here.

class Booking(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_CONFIRMED = 'confirmed'
    STATUS_CANCELLED = 'cancelled'
    STATUS_REJECTED = 'rejected'
    STATUS_COMPLETED = 'completed'
    
    STATUS_CHOICES = [
        
         (STATUS_PENDING, 'pending'),
    (STATUS_CONFIRMED, 'confirmed'),
    (STATUS_CANCELLED, 'cancelled'),
    (STATUS_REJECTED, 'rejected'),
    (STATUS_COMPLETED, 'completed')
    ]
    
    # link a booking to a client profile
    
    client = models.ForeignKey(
        'client.Client',
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    # link a booking to an architect profile
    architect = models.ForeignKey(
        'architects.Architect',
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_at',)
        indexes = [
            models.Index(fields=['architect', 'appointment_date']),
        ]
    def __str__(self):
        
        return f"booking {self.id} - {self.client.user.username} -> {self.architect.username} on {self.appointment_date}"