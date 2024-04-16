from django.db import models

# Create your models here.

class UserAuth(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.username

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1500)
    photo = models.ImageField(upload_to='static/%Y/%M/%d/')
    time_post = models.DateTimeField(auto_created=True)
    def __str__(self) -> str:
        return self.title


class SearchItem(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=20)

