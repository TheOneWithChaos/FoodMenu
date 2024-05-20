from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.CharField(max_length=1000, default='https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
         return reverse('detail', kwargs={'pk':self.pk})