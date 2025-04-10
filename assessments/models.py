from django.db import models
from django.conf import settings
# Create your models here.

class PersonalityTest(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assessment_tests'
    )

class Question(models.Model):
    text = models.CharField(max_length=255)
    trait = models.CharField(max_length=2) # O, C, E, A, N