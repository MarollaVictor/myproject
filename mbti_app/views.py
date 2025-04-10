from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PersonalityTest
from django.conf import settings

class UserProfileView(LoginRequiredMixin, DetailView):
    model = PersonalityTest
    template_name = 'mbti_app/user_profile.html'
    context_object_name = 'personality_test'
    
    def get_object(self):

        return self.request.user.personality_test

class AssessmentView(LoginRequiredMixin, TemplateView):
    template_name = 'mbti_app/assessment.html'

class RecommendationsView(LoginRequiredMixin, TemplateView):
    template_name = 'mbti_app/recommendations.html'