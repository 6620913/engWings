from django.db import models

# Create your models here.

class Videos(models.Model):
    title = models.CharField()
    video =models.FileField(upload_to="wings/%y")
    udate =models.CharField()
    disc  =models.TextField()

    def __str__(self):
        return self.title