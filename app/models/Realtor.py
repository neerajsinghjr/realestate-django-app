#------------------------------------------------------#
# REALTOR MODEL
#------------------------------------------------------#

from datetime import datetime as date
from django.db import models as Schema


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

