from rest_framework import serializers
from .models import Pelicula, Director

class PeliculaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pelicula
        fields = ['id','nombre','descripcion','anio_lanzamiento','director','url_portada']

class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Director
        fields = ['id','nombre']