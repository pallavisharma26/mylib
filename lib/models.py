from django.db import models
import os



class Actor(models.Model):
    actor_name = models.CharField(max_length=100)

    def __str__(self):
        return self.actor_name
   
   
class Genre(models.Model):
    genre_type = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_type

class Movie(models.Model):
    movie_title = models.CharField(max_length=100)
    actors_name = models.ForeignKey(Actor, on_delete=models.CASCADE)
    genre_type = models.ForeignKey(Genre, on_delete=models.CASCADE)
    release_date = models.DateField()
    running_time = models.TimeField()
    movie_discription = models.TextField()
    

    def __str__(self):
        return self.movie_title

    



