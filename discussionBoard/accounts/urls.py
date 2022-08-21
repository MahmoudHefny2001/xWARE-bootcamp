from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.contrib import admin
from accounts import views


urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login')
]
