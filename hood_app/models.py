from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Neighbourhood(models.Model):
    name=models.CharField(max_length=60)
    location=models.CharField(max_length=60)
    population=models.IntegerField()
    image = models.ImageField(upload_to = 'images/')

class Profile(models.Model):
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio=models.CharField(max_length=300)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
