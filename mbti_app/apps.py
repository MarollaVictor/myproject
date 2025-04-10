# mbti_app/apps.py
from django.apps import AppConfig
from django.conf import settings

class MBTIAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mbti_app'  # Full Python path to your app