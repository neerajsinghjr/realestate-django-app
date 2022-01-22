#------------------------------------------------------#
# USER MODEL
#------------------------------------------------------#

from datetime import datetime as date
from django.db import models as Schema


class User(Schema.Model):
    #-------------------
    # Models Attributes
    #-------------------
    name = Schema.CharField(max_length=256)
    email = Schema.CharField(max_length=512)
    phone = Schema.CharField(max_length=20)
    created = Schema.DateTimeField(default=date.now, blank=True)

    #----------------
    # Models Methods
    #----------------
    def __str__(self):
        return (f"User {self.name}")
