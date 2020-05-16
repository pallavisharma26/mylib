from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('movies/<str:rating>', views.movies, name='movie_page'),
    path('musics/<str:rating>', views.musics, name='music_page'),
    path('books/<str:rating>', views.books, name='book_page'),
    path('pictures/<str:type>', views.pictures, name='picture_page'),
]
