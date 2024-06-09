from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg', upload_to='pictures/profile_pics')
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
