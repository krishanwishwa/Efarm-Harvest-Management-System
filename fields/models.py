from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from osm_field.fields import LatitudeField, LongitudeField, OSMField

class Fields(models.Model):

    soiltype = (
        ('clay', 'clay'),
        ('loamy', 'loamy'),
        ('sandy', 'sandy'),
        ('silty', 'silty'),
    )

    ownertype = (
        ('lease', 'lease'),
        ('private', 'private'),
        ('mixed', 'mixed'),
        ('other', 'other'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    field_number = models.CharField(max_length=17,blank=True)
    address = models.CharField(max_length=100,blank=True)
    crop_product = models.CharField(max_length=100)
    usable_area = models.CharField(max_length=100)
    soil_type = models.CharField(max_length=11,default='clay',choices=soiltype)
    ownership_type = models.CharField(max_length=11,default='private',choices=ownertype)
    location = OSMField()
    location_lat = LatitudeField()
    location_lon = LongitudeField()

    def __str__(self):
        return self.address
