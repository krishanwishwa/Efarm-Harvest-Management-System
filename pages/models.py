from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Product(models.Model):
    product = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, default='')
    contact_number = models.CharField(max_length=17,blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    body = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.product
