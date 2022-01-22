#------------------------------------------------------#
# LISTING MODEL
#------------------------------------------------------#

from .Realtor import Realtor 
from datetime import datetime as date
from django.db import models as Schema


class Listing(Schema.Model):

    #-------------------
    # Model Attributes
    #-------------------

    # Table Key
    realtor_id = Schema.ForeignKey(Realtor, on_delete=Schema.DO_NOTHING)
    title = Schema.CharField(max_length=256)
    address = Schema.CharField(max_length=512)
    city = Schema.CharField(max_length=256)
    state = Schema.CharField(max_length=256)
    pincode = Schema.CharField(max_length=32)
    descripton = Schema.TextField(blank=True)
    price = Schema.IntegerField()
    bedrooms = Schema.IntegerField()
    bathrooms = Schema.IntegerField()
    garage = Schema.IntegerField(default=0)
    sqft = Schema.IntegerField()
    published = Schema.BooleanField(default=True)
    created = Schema.DateTimeField(default=date.now, blank=True)

    # Media
    photo_bg = Schema.ImageField(upload_to='listings/%Y/%m/%d/', blank=True)
    photo_1 = Schema.ImageField(upload_to='listings/%Y/%m/%d/', blank=True)
    photo_2 = Schema.ImageField(upload_to='listings/%Y/%m/%d/', blank=True)
    photo_3 = Schema.ImageField(upload_to='listings/%Y/%m/%d/', blank=True)
    photo_4 = Schema.ImageField(upload_to='listings/%Y/%m/%d/', blank=True)
    photo_5 = Schema.ImageField(upload_to='listings/%Y/%m/%d/', blank=True)

    #-----------------
    # Models Methods
    #-----------------
    def __repr__(self):
        return (f"Listing <'class'> {self.title}")

