from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from django.urls import reverse
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType
from users.models import Profile

# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to='gala/',blank=True)
    date_posted = models.DateTimeField(default=timezone.now) 
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE,null=True)

    def __str__(self):
        return self.title
