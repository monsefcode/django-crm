from django.shortcuts import render
# models
from .models import Profile, Project
# generic views
from django.views.generic import ListView
# mixin
from django.contrib.auth.mixins import LoginRequiredMixin

'''
 - Profiles views
'''

def home_page(request):
    return render(request, 'management/home.html')

class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'management/profiles.html'
    context_object_name = 'profiles'
    login_url = 'login'