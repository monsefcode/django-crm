from django.urls import path, include # new
from .views import home_page, ProfileListView

urlpatterns = [
    path('', home_page, name='home'),
    path('profiles/', ProfileListView.as_view(), name='profiles'),
]
