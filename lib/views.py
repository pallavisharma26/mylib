from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


def index(request):
    return render(request,'lib/index.html')

def text(request):
    return render(request,'lib/text.html')
    
# def movies(request):
#     return render(request,'lib/movie.html')

# def musics(request, rating):
#     return render(request,'lib/music.html')

# def books(request, rating):
#     return render(request,'lib/book.html')

# def pictures(request, type):
#     return render(request,'lib/picture.html')

