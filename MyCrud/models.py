from django.db import models

# Create your models here.

class UserAuth(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1500)
    photo = models.ImageField(upload_to='/yy/mm/dd')
    time_post = models.DateTimeField(auto_created=True)
    


