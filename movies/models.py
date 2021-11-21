from django.db import models

class Movie(models.Model):
    title= models.CharField(max_length=50)
    description = models.TextField()
    realese_date = models.DateTimeField()
    cast = models.ManyToManyField('Cast', null= True, blank=True)
    cat = models.ManyToManyField('Category', null= True, blank=True)
    panner = models.ImageField(upload_to= 'movies/panner', null= True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=50)

class Cast(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    age = models.IntegerField()

class Series(Movie):
    season = models.IntegerField()
    eposide = models.IntegerField()