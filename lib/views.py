from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies


def index(request):
    return render(request,'lib/index.html')
    
def movies(request):
    return render(request,'lib/movie.html')

def musics(request):
    return render(request,'lib/music.html')

def books(request):
    return render(request,'lib/book.html')

def pictures(request):
    return render(request,'lib/picture.html')

