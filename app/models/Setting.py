#------------------------------------------------------#
# SETTING MODEL
#------------------------------------------------------#
from django.db import models as Schema
from datetime import datetime as date


class Setting(Schema.Model):
    appName = Schema.CharField(default="BT Real Estate", max_length=512)
    appEmail = Schema.CharField(default="", max_length=512)
    appAbout = Schema.TextField(blank='')
    facebook = Schema.CharField(max_length=512)
    twitter = Schema.CharField(max_length=512)              
    linkedin = Schema.CharField(max_length=512)             
    pinterest = Schema.CharField(max_length=512)                
    whatsapp = Schema.CharField(max_length=512)             
    instagram = Schema.CharField(max_length=512)                
    youtube = Schema.CharField(max_length=512)              
    created = Schema.DateTimeField(default=date.now, blank=True)

    def __repr__(self):
        return (f"Setting {self.appName}")

