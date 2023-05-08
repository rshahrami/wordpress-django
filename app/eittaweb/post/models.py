from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class PostModel(models.Model):
    like = models.IntegerField(default=10, validators=[
        MaxValueValidator(2000),
        MinValueValidator(1)
    ])
    image = models.ImageField(upload_to='post')
    text = models.TextField(default='#ایران_ما')
    name = models.CharField(max_length=50, default='ادمین')
    date = models.DateField(auto_now_add=True)

# Create your models here.

