from django.forms import ModelForm
from .models import Product
from django import forms

class Productform(ModelForm):
    class Meta:
        model = Product
        fields = [  'product',
                    'email',
                    'contact_number',
                    'date',
                    'body',
                    'price',
                    'image',
                    ]
