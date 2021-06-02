from django.forms import ModelForm
from .models import Sales
from .models import Expenses
from django import forms

class Salesform(ModelForm):
    class Meta:
        model = Sales
        fields = [  'sales_number',
                    'customer',
                    'product',
                    'quantity',
                    'payment_method',
                    'date',
                    'payment',
                    ]

class Expenseform(ModelForm):
    class Meta:
        model = Expenses
        fields = [  'expense_number',
                    'item',
                    'quantity',
                    'payment_method',
                    'date',
                    'payment',
                    'description',
                    ]
