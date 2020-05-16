from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies


def index(request):
    return render(request,'lib/index.html')
<<<<<<< HEAD
    
def movies(request):
=======

def movies(request, rating):
>>>>>>> 3d65a0ee80ae25b4966bd2fdaeff851cf2fa699f
    return render(request,'lib/movie.html')

def musics(request, rating):
    return render(request,'lib/music.html')

def books(request, rating):
    return render(request,'lib/book.html')

def pictures(request, type):
    return render(request,'lib/picture.html')

