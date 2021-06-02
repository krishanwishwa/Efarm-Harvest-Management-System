from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    accountChoices = (
        ('F', 'Farmer'),
        ('I', 'Instructor'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='images/')
    type = models.CharField(max_length=1,default='F',choices=accountChoices)
    address = models.CharField(max_length=200,blank=True)
    city = models.CharField(max_length=100,blank=True)
    state = models.CharField(max_length=100,blank=True)
    zipcode = models.CharField(max_length=20,blank=True)
    contact_number = models.IntegerField(blank=True,null=True)


    def __str__(self):
        return self.user.username
