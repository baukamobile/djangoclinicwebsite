from django.db import models

# Create your models here.
class Items(models.Model):
    items = models.CharField(max_length=100)

    class Meta:
        ordering = ['items']

    def __str__(self):
        return self.items