from django.db import models
import os

class Movies(models.Model):
    name = models.CharField(max_length=30)
    criteria = models.CharField(max_length=30)
    

def __str__(self):
        return self.name
   
   
