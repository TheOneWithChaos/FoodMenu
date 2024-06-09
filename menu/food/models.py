from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.CharField(max_length=1000, default='https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self): # get_absolute_url is a method that returns the url to the detail page of the object, it is needed for the CreateView to work
         return reverse('food:detail', kwargs={'pk':self.pk}) #reverse is a function that returns the full url to a given view, it takes the view name and the kwargs as arguments