from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')
    location = models.CharField(max_length=100)
    user_type = models.CharField(max_length=200, default='users')

    def __str__(self):
        return self.user.username
    

class CusRatingFeedback(models.Model):
    prod_code = models.IntegerField(default=1)
    ratings = models.FloatField()
    feedback = models.CharField(max_length=200)
    user_type = models.CharField(max_length=200, default='users')

    def __str__(self):
        return str((str(self.prod_code), 
                str(self.ratings), 
                str(self.feedback), 
                str(self.user_type)))
                