from django.forms import ModelForm
from .models import Workers
from .models import Machines
from django import forms

class Workersform(ModelForm):
    class Meta:
        model = Workers
        fields = [  'name',
                    'gender',
                    'position',
                    'employee_number',
                    'address',
                    'email',
                    'contact_number',
                    ]

class Machinesform(ModelForm):
    class Meta:
        model = Machines
        fields = [  'machine_number',
                    'category',
                    'manufacturer',
                    'model',
                    'year',
                    'reg_number',
                    ]
