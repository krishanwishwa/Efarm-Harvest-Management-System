from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Sales(models.Model):

    salestype = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Credit Card', 'Credit Card'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sales_number = models.CharField(max_length=17,blank=True)
    customer = models.CharField(max_length=17,blank=True)
    product = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=11,default='Cash',choices=salestype)
    date = models.DateTimeField(default=datetime.now, blank=True)
    payment = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product

class Expenses(models.Model):

    expensetype = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Credit Card', 'Credit Card'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense_number = models.CharField(max_length=17,blank=True)
    item = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=11,default='Cash',choices=expensetype)
    date = models.DateTimeField(default=datetime.now, blank=True)
    payment = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.item
