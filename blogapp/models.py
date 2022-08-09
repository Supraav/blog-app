from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField(max_length=1000)
    date_posted=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE) #if user is deleted then delete the post 
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['date_posted']



        # TestUser[Testing123@]