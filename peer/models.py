from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
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
    project_link = models.URLField(unique=True, blank = True, null =True)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
    
    @property
    def design_votes(self):
       if self.votes.count() == 0:
           return 5
       return sum([r.design_votes for r in self.votes.all()]) / self.votes.count()

        
    @property
    def content_votes(self):
       if self.votes.count() == 0:
           return 5
       return sum([r.content_votes for r in self.votes.all()]) / self.votes.count()    

    @property
    def usability_votes(self):
       if self.votes.count() == 0:
           return 5
       return sum([r.usability_votes for r in self.votes.all()]) / self.votes.count()

        
    @property
    def creativity_votes(self):
       if self.votes.count() == 0:
           return 5
       return sum([r.creativity_votes for r in self.votes.all()]) / self.votes.count()

class Vote(models.Model):

    ratings = (1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9),(10, 10)

    project = models.ForeignKey(Project, related_name = 'votes', on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    design_votes = models.IntegerField(choices = ratings, default = 0)
     
    content_votes = models.IntegerField(choices = ratings, default = 0)
    usability_votes = models.IntegerField(choices = ratings, default = 0)
    creativity_votes = models.IntegerField(choices = ratings, default = 0)
    

    def __str__(self):
        return f'design {self.design_votes} usability {self.usability_votes} content {self.content_votes} creativity {self.creativity_votes}'


    def get_absolute_url(self):
        return reverse('welcome')    



