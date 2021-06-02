from django.forms import ModelForm
from .models import Fields
from django import forms

class Fieldsform(ModelForm):
    class Meta:
        model = Fields
        fields = [
                    'field_number',
                    'address',
                    'crop_product',
                    'usable_area',
                    'soil_type',
                    'ownership_type',
                    'location',
                    'location_lat',
                    'location_lon',
                    ]
