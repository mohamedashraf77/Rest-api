from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('movies', views.movies_index, name= 'movies'),
    path('movie/<int:id>', views.movie_index, name= 'movie'),
    path('create', views.create_movie, name= 'create'),
    path('delete/<int:id>', views.delete_movie, name= 'delete'),
    path('update/<int:id>', views.update_movie, name= 'update'),
]