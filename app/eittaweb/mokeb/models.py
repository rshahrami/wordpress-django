from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class PooyeshMokebModel(models.Model):
    like = models.IntegerField(default=10, validators=[
        MaxValueValidator(2000),
        MinValueValidator(1)
    ])
    image = models.ImageField(upload_to='mokeb')
    text = models.TextField(default='#موکب_کودکانه')
    name = models.CharField(max_length=50, default='ادمین')
    date = models.DateField(auto_now_add=True)
