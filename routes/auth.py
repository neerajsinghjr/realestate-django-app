############################################################
# AUTH ROUTES
############################################################

from django.contrib import *
from django.urls import path
from app.controllers.WebController.AuthController import AuthController 


auth = AuthController()

# Auth Routes;
authRoutes = [
    path('', auth.login, name="admin.login"),                   # ~ fallback 
    path('login', auth.login, name="admin.login"),
    path('register', auth.register, name="admin.register"),
    path('forget', auth.forget, name="admin.forget"),
]

# Global Routes;
urlpatterns = authRoutes               # Concatenates or Add new routes;

