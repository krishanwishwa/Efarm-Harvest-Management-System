from django.db import models
from django.contrib.auth.models import User


class Workers(models.Model):

    genderChoices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employee_number = models.CharField(max_length=17,blank=True)
    name = models.CharField(max_length=100,blank=True)
    position = models.CharField(max_length=100,blank=True)
    gender = models.CharField(max_length=1,default='M',choices=genderChoices)
    address = models.CharField(max_length=200,blank=True)
    email = models.EmailField(max_length=254, default='')
    contact_number = models.CharField(max_length=17,blank=True)
    add_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Machines(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    machine_number = models.CharField(max_length=17,blank=True)
    category = models.CharField(max_length=100,blank=True)
    manufacturer = models.CharField(max_length=100,blank=True)
    model = models.CharField(max_length=200,blank=True)
    year = models.IntegerField(blank=True,null=True)
    reg_number = models.CharField(max_length=17,blank=True)


    def __str__(self):
        return self.category
