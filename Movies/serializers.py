
from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields =['id','director', 'name', 'desc']
        # fields = '__all__'