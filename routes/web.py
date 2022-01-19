############################################################
# WEB ROUTES
############################################################

from django.contrib import *
from django.urls import path


from app.controllers.WebController.HomeController import HomeController


home = HomeController()

# WebController Routes
webRoutes = [
    path('', home.index, name='index'),
    path('about', home.about, name='about'),
    path('contact', home.contact, name='contact'),
    path('search', home.search, name='search'),
    path('dashboard', home.dashboard, name="dashboard"),
    path('listings', home.listings, name="listings"),
    path('listing/<eid>', home.listing, name="listing"),
]

# App Routes;
urlpatterns = webRoutes                 # Concatenates or Add new routes;