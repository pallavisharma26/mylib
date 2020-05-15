from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=30)
    review = models.CharField(max_length=30)

  
   
