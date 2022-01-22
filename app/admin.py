from curses.ascii import US
from django.contrib import admin
# from django.apps import apps
from .models import *

# models = apps.get_models()


# Register your models here.
admin.site.register(Listing)
admin.site.register(Realtor)
admin.site.register(User)

