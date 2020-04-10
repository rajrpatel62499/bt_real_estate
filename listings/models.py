from datetime import datetime

from django.db import models

# Create your models here.
from realtors.models import Realtor


class Listing(models.Model):
    realtor = models.ForeignKey(to=Realtor,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    description = models.TextField( blank=True) # blank = True means it is optional
    price = models.IntegerField()

    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2,decimal_places=1)
    garage = models.IntegerField(default=0) # it will set default value 0 to database
    sqft = models.IntegerField()
    lotsize = models.DecimalField(max_digits=5,decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.title
