from django.db import models

# Create your models here.

class Videos(models.Model):
    thumbnail = models.ImageField(upload_to="pics")
    title = models.CharField(max_length=200)
    video =models.FileField(upload_to="wings/%y")
    udate =models.CharField(max_length=100)
    disc  =models.TextField()

    def __str__(self):
        return self.title