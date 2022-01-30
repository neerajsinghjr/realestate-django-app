#------------------------------------------------------#
# LISTING MODEL
#------------------------------------------------------#

from .Realtor import Realtor 
from datetime import datetime as date
from django.db import models as Schema
from cryptography.fernet import Fernet
from django.conf import settings


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
    '''
    @class info
    '''
    def __repr__(self):
        return (f"Listing <'class'> {self.title}")

    '''
    @return encryptedId;
    '''
    def encrypt(id):
        cipher_suite = Fernet(settings.ENCRYPT_KEY)         # Byte Key
        encrypted_text = cipher_suite.encrypt(txt.encode('ascii'))
        return encrypted_text
        # try:
        #     if not id:
        #         return "PK not found"
        #     txt = str(id)
        #     cipher_suite = Fernet(settings.ENCRYPT_KEY) # key should be byte
        #     encrypted_text = cipher_suite.encrypt(txt.encode('ascii'))
        #     encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii") 
        #     return encrypted_text
        # except Exception as e:
        #     logging.getLogger("error_logger").error(traceback.format_exc())
        #     return None
