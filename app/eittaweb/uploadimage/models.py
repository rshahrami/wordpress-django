from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class UploadImageModel(models.Model):
    image = models.ImageField(upload_to='uploadimage')
    name = models.CharField(max_length = 200)
    number = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)