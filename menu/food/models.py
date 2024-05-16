from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.CharField(max_length=1000, default='https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg')

    def __str__(self):
        return self.name