#------------------------------------------------------#
# USER MODEL
#------------------------------------------------------#

from datetime import datetime as date
from django.db import models as Schema


class Customer(Schema.Model):

    #-------------------
    # Model Attributes
    #-------------------    

    # Table Key
    name = Schema.CharField(max_length=256)
    username = Schema.CharField(max_length=512,null=True, default='user')
    phone = Schema.CharField(max_length=20, null=True, default='123-456-7890')
    email = Schema.CharField(max_length=512)
    password = Schema.TextField(blank=True)
    descripton = Schema.TextField(blank='')
    avatar = Schema.ImageField(upload_to='users/%Y/%m/%d/', blank="avatar.png")
    created = Schema.DateTimeField(default=date.now, blank=True)

    #-----------------
    # Models Methods
    #-----------------
    def __repr__(self):
        return (f"User <'class'> {self.name}")

    