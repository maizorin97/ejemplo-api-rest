from django.contrib import admin
from .models import Pelicula, Director


class PeliculaAdmin(admin.ModelAdmin):
    readonly_fields = ()
    list_display = ('id','nombre','descripcion','anio_lanzamiento','director','url_portada')
admin.site.register(Pelicula, PeliculaAdmin)


class DirectorAdmin(admin.ModelAdmin):
    readonly_fields = ()
    list_display = ('id','nombre')
admin.site.register(Director, DirectorAdmin)
