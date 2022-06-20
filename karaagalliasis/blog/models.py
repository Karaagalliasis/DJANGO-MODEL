from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Post(models.Model):

    Title= models.CharField(max_length=200)

    Text= models.TextField(max_length=200)
    
    Author= models.ForeignKey('self', get_user_model())

    Created_date= models.DateTimeField

    Published_date= models.DateTimeField