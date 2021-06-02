from django.forms import ModelForm
from .models import UserProfile
from django import forms

class UserProfileForm(ModelForm):


    class Meta:
        model = UserProfile
        fields = [  'image',
                    'type',
                    'address',
                    'city',
                    'state',
                    'zipcode',
                    'contact_number',
                    ]
