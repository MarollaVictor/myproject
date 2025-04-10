from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    # Custom fields (profile data)
   # Critical MVP Fields
    opt_in_ml = models.BooleanField(default=True)  # For privacy compliance
    last_activity = models.DateTimeField(auto_now=True)  # For engagement tracking
    
    # Simplified Profile Fields
    bio = models.CharField(max_length=160, blank=True, null=True)  # CharField instead of TextField
    goals = models.JSONField(default=list)  # Default empty list
    
    # Emergency Contact (for password reset)
    recovery_email = models.EmailField(blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['username']),  # Faster login lookups
        ]

    def __str__(self):
        return self.email or self.username  # Better admin display


    