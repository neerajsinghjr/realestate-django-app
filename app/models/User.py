#------------------------------------------------------#
# USER MODEL
#------------------------------------------------------#

from datetime import datetime as date
from django.db import models as Schema


class User(Schema.Model):

    #-------------------
    # Model Attributes
    #-------------------    

    # Table Key
    name = Schema.CharField(max_length=256)
    phone = Schema.CharField(max_length=20, blank='')
    email = Schema.CharField(max_length=512)
    descripton = Schema.TextField(blank=True)
    created = Schema.DateTimeField(default=date.now, blank=True)
    avatar = Schema.ImageField(upload_to='users/%Y/%m/%d/', blank="avatar.png")

    #-----------------
    # Models Methods
    #-----------------
    def __repr__(self):
        return (f"User <'class'> {self.name}")

