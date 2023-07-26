from django.shortcuts import render
from .models import Movie
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import MovieSerializer
# Create your views here.

class MovieListView(ListCreateAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer