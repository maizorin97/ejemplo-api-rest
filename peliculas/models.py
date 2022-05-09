from django.db import models

class Director(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)

class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    anio_lanzamiento = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    url_portada = models.CharField(max_length=500)
