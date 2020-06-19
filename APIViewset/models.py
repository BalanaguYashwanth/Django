from django.db import models


# Create your models here.
class details(models.Model):
    person=models.CharField(max_length=150)
    zone=models.CharField(max_length=150)
    place=models.CharField(max_length=150)

    