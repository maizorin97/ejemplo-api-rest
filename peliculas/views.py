from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Pelicula, Director
from .serializers import PeliculaSerializer, DirectorSerializer
from rest_framework import permissions


class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    permission_classes = [IsAuthenticated]

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated]