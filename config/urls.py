from django.contrib import admin                    # Admin Backend;
from django.urls import path, include               # Url, Path;
from django.conf.urls.static import static          # Static Content Loads;
from django.conf import settings                    # App Settings;

# from config import settings


# Admin Routes Init;
adminRoutesInit = [
    path('admin/', include('routes.admin')),     # Admin Routes;
]

# Auth Routes Init;
authRoutesInit = [
    path('auth/', include('routes.auth')),       # Auth Routes;
]

# Web Routes Init;
webRoutesInit = [
    path('', include('routes.web')),             # Web Routes;
]

# Static Content Routes Init
staticRoutesInit = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Global Routes;
urlpatterns = authRoutesInit + adminRoutesInit + webRoutesInit + staticRoutesInit
