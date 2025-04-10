from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import User
from django.conf import settings

# Create your views here.
class SignUpView(CreateView):
    model = User
    template_name = 'users/signup.html'
    fields = ['username', 'email', 'password1', 'password2']
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = 'users/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')
    
    