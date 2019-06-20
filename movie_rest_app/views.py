from rest_framework import viewsets
from . import models
from . import serializers

class GenreViewset(viewsets.ModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer

class MovieDetailViewset(viewsets.ModelViewSet):
    queryset = models.MovieDetail.objects.all()
    serializer_class = serializers.MovieDetailSerializer