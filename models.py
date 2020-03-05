from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class data(models.Model):
    user=models.OneToOneField(to=User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    




    
