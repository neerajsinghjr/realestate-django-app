############################################################
# Admin Routes
############################################################
from django.contrib import admin
from django.urls import path


# Admin URL
urlpatterns = [
    path('', admin.site.urls),
]