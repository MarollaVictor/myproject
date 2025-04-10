# recommendations/urls.py
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
]
