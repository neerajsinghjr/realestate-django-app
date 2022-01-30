from csv import list_dialects
from curses.ascii import US
from django.contrib import admin
# from django.apps import apps
from .models import *


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published', 'price', 'address', 'city', 'state', 'created')
    list_link = ('id', 'title')
    list_filter = ('city', 'state')
    list_editable = ('published',)
    list_per_page = 25
    list_max_show_all = 50
    search_fields = ('title', 'address', 'city', 'state', 'address')

    
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'top_seller', 'created')
    list_link = ('id', 'name', 'email')
    list_filter = ('top_seller',)
    search_fields = ('id', 'name', 'email')
    list_per_page = 25
    list_max_show_all = 50
    list_editable = ('top_seller',)


# REGISTER MODEL AND ADMIN SCHEMA;
admin.site.register(Listing, ListingAdmin)
admin.site.register(Realtor, RealtorAdmin)
admin.site.register(User)
