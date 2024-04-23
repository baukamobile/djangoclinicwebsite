from django.db import models
from django_google_maps import fields as map_fields

# Create your models here.


class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)


    
class UserAuth(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.username

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1500)
    photo = models.ImageField(upload_to='static/')
    time_post = models.DateTimeField(auto_created=True)
    def __str__(self) -> str:
        return self.title


class SearchItem(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=20)

    def __str__(self):
        return self.title



class Upload(models.Model):
    name = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name
    