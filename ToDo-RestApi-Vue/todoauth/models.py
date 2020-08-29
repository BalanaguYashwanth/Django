from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):             #dummy profile not used 
    user = models.OneToOneField(User, on_delete=models.CASCADE)   #dummy profile 



    
