from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_lenth = 150)
    location = models.CharField(max_length = 150)
    occupants_count = models.CharField(max_length = 150)


    
