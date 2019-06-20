# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Genre(models.Model):
    """  Genre model """
    name = models.CharField(max_length=500)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name

class MovieDetail(models.Model):
    """ MovieDetails model """
    name = models.CharField(max_length=500)
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    director = models.CharField(max_length=500)
    genre = models.ManyToManyField(Genre)

    class Meta:
        verbose_name = "MovieDetail"
        verbose_name_plural = "MovieDetails"

    def __str__(self):
        return self.name