from django import forms
from osm_field.fields import LatitudeField, LongitudeField, OSMField

#search function
class SearchForm(forms.Form):
    # latitude = forms.DecimalField (required= True,label='Latitude',initial=6.927079,max_value=90, min_value=-90,)
    # longitude = forms.DecimalField (required= True,label='Longitude',initial= 79.861244, max_value=180, min_value=-180,)




    location = OSMField()
    latitude = LatitudeField()
    longitude = LongitudeField()
