from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('movies/', views.movies, name='movie_page'),
    path('musics/', views.musics, name='music_page'),
    path('books/', views.books, name='book_page'),
    path('pictures/', views.pictures, name='picture_page'),
]
