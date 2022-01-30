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
    path('register', auth.register, name="auth.register"),
    path('forget', auth.forget, name="auth.forget"),
]

# Global Routes;
urlpatterns = authRoutes               # Concatenates or Add new routes;

