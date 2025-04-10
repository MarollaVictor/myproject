from django.db import models
from django.conf import settings


# MBTI Personality Types (e.g., INFJ, ENTP)

class PersonalityTest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mbti_tests')
    opennes = models.FloatField()
    conscientiousness = models.FloatField()
    extraversion = models.FloatField()
    agreeableness = models.FloatField()
    neuroticism = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Meta:
    ordering = ['-timestamp']  # Newest first
    def __str__(self):
        return f"{self.user.username}'s OCEAN Results"

class MBTIType(models.Model):
    type_code = models.CharField(max_length=4, unique=True)  # e.g., "INTJ"
    name = models.CharField(max_length=50)                   # e.g., "The Architect"
    description = models.TextField()

    def __str__(self):
        return self.type_code

# Personality Test Questions
class Question(models.Model):
    DICHOTOMIES = [
        ('EI', 'Extraversion vs Introversion'),
        ('SN', 'Sensing vs Intuition'),
        ('TF', 'Thinking vs Feeling'),
        ('JP', 'Judging vs Perceiving'),
    ]
    
    text = models.CharField(max_length=200)
    dichotomy = models.CharField(max_length=2, choices=DICHOTOMIES)  # Which MBTI axis it measures
    direction = models.SmallIntegerField(default=1)  # 1 or -1 (affects scoring polarity)

    def __str__(self):
        return self.text

# User Responses
class UserResponse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)  # Allow anonymous
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.SmallIntegerField()  # Typically 1-5 scale (1=Strongly Disagree, 5=Strongly Agree)
    timestamp = models.DateTimeField(auto_now_add=True)

# Test Results
class TestResult(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    mbti_type = models.ForeignKey(MBTIType, on_delete=models.CASCADE)
    ei_score = models.FloatField()  # E vs I score
    sn_score = models.FloatField()  # S vs N score
    tf_score = models.FloatField()  # T vs F score
    jp_score = models.FloatField()  # J vs P score
    timestamp = models.DateTimeField(auto_now_add=True)

    def calculate_mbti(self):
        """Convert scores to 4-letter MBTI type"""
        type_code = []
        for score, pair in zip(
            [self.ei_score, self.sn_score, self.tf_score, self.jp_score],
            ['EI', 'SN', 'TF', 'JP']
        ):
            type_code.append(pair[0] if score > 0 else pair[1])
        return ''.join(type_code)
