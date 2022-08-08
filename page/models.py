from django.db import models
from django.forms import ImageField

# Create your models here.
class Team(models.Model):
    firstname=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='photos')
    description=models.TextField(max_length=200)
    facebook=models.URLField(max_length=100)
    twitter=models.URLField(max_length=100)
    google=models.URLField(max_length=50)


def __str__(self):
    return self.firstname
