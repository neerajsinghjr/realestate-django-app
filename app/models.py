
# from .Realtor import Realtor 
from datetime import datetime as date
from django.db import models as Schema



#------------------------------------------------------#
# REALTOR MODEL
#------------------------------------------------------#

class Realtor(Schema.Model):

    #-------------------
    # Model Attributes
    #-------------------    
    # Table Key
    name = Schema.CharField(max_length=256)
    phone = Schema.CharField(max_length=20)
    email = Schema.CharField(max_length=512)
    descripton = Schema.TextField(blank=True)
    top_seller = Schema.BooleanField(default=False)
    created = Schema.DateTimeField(default=date.now, blank=True)
    # Media Key
    avatar = Schema.ImageField(upload_to='realtors/%Y/%m/%d/')

    #-----------------
    # Models Methods
    #-----------------
    def __repr__(self):
        return (f"Realtor 'class' {self.name}")


#------------------------------------------------------#
# LISTING MODEL
#------------------------------------------------------#

class Listing(Schema.Model):

    #-------------------
    # Model Attributes
    #-------------------
    # Foreign Key
    realtor_id = Schema.ForeignKey(Realtor, on_delete=Schema.DO_NOTHING)
    # General Key
    title = Schema.CharField(max_length=256)
    address = Schema.CharField(max_length=512)
    city = Schema.CharField(max_length=256)
    state = Schema.CharField(max_length=256)
    pincode = Schema.CharField(max_length=32)
    descripton = Schema.TextField(blank=True)
    price = Schema.IntegerField()
    bedrooms = Schema.IntegerField()
    bathrooms = Schema.IntegerField(max_digits=2, decminal_places=1)
    garage = Schema.IntegerField(default=0)
    sqft = Schema.IntegerField()
    published = Schema.BooleanField(default=True)
    created = Schema.DateTimeField(default=date.now, blank=True)
    # Media
    photo_bg = Schema.ImageField(upload_to='listings/%Y/%m/%d/')
    photo_1 = Schema.ImageField(upload_to='listings/%Y/%m/%d/')
    photo_2 = Schema.ImageField(upload_to='listings/%Y/%m/%d/')
    photo_3 = Schema.ImageField(upload_to='listings/%Y/%m/%d/')
    photo_4 = Schema.ImageField(upload_to='listings/%Y/%m/%d/')
    photo_5 = Schema.ImageField(upload_to='listings/%Y/%m/%d/')

    #-----------------
    # Models Methods
    #-----------------
    def __repr__(self):
        return (f"Listing 'class' {self.title}")





