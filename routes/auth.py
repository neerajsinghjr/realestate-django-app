############################################################
# AUTH ROUTES
############################################################

from django.contrib import *
from django.urls import path
from app.controllers.WebController.AuthController import AuthController 


auth = AuthController()

# Auth Routes;
authRoutes = [
    path('', auth.login, name="auth.login"),                   # ~ fallback 
    path('login', auth.login, name="auth.login"),
    path('logout', auth.logout, name="auth.logout"),
    path('register', auth.register, name="auth.register"),
    path('forget', auth.forget, name="auth.forget"),
    path('reset-password', auth.resetPassword, name="auth.reset"),
    path('dashboard', auth.dashboard, name='auth.dashboard')
]

# Global Routes;
urlpatterns = authRoutes               # Concatenates or Add new routes;

