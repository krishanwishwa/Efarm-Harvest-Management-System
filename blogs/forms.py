from django.forms import ModelForm
from .models import Blog
from django import forms

class Blogform(ModelForm):
    class Meta:
        model = Blog
        fields = [  'title',
                    'content',
                    'user',
                    'image',
                    ]
