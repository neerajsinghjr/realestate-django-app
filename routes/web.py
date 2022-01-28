############################################################
# WEB ROUTES
############################################################

from django.contrib import *
from django.urls import path


from app.controllers.WebController.HomeController import HomeController


home = HomeController()

# WebController Routes
webRoutes = [
    path('', home.index, name='home'),
    path('about', home.about, name='about'),
    path('contact', home.contact, name='contact'),
    path('search', home.search, name='search'),
    path('dashboard', home.dashboard, name="dashboard"),
    path('listings', home.listings, name="listings"),
    path('listing/<eid>', home.listing, name="listing"),
    path('httpback', home.httpBack, name="http.back"),
    path('realtor/<eid>', home.realtor, name="realtor"),
]

# App Routes;
urlpatterns = webRoutes                 # Concatenates or Add new routes;