from django.db import models
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Profile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_img= models.ImageField(default="default.jpg",upload_to='gala/')

    def __str__(self):
        return f'{self.user.username} Profile'

    
# Create your models here.
