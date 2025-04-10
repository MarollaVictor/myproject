# mbti_app/urls.py
from django.urls import path
from . import views
from django.conf import settings

app_name = 'mbti_app'

urlpatterns = [
    # Profile
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    
    # Assessment Flow
    path('assessment/', views.AssessmentView.as_view(), name='assessment'),
    
    # Recommendations
    path('recommendations/', views.RecommendationsView.as_view(), name='recommendations'),
]
