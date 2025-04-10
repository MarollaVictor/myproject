from django.db import models
from django.conf import settings

# Create your models here.

class Habit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    trait = models.CharField(max_length=2) # Linked to personality traits


class DailySchedule(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    habit = models.ForeignKey('Habit', on_delete=models.CASCADE)
    scheduled_time = models.TimeField()
    
    
    