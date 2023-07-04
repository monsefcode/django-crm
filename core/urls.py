from django.urls import path
from django.contrib.auth import views as auth_views
import core.views as core_views

urlpatterns = [
    path('register/', core_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    # path('password-reset/',
    #      auth_views.PasswordResetView.as_view(template_name='auth/password_reset.html'),
    #      name='password_reset'),
]