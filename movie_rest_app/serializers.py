from rest_framework import serializers
from .models import MovieDetail, Genre

class GenreSerializer(serializers.ModelSerializer):
    ########## Serializer class for Genre ##########
    class Meta:
        model = Genre
        fields = '__all__'

class MovieDetailSerializer(serializers.ModelSerializer):
    ########## Serializer class for MovieDetail ##########
    genre = GenreSerializer(many=True)

    class Meta:
        model = MovieDetail
        fields = ('name', 'imdb_score', 'popularity', 'director', 'genre')