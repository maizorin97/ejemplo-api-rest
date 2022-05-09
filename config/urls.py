from django.contrib import admin
from django.urls import path, include
from peliculas import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'producto', views.PeliculaViewSet,basename='producto')
router.register(r'director', views.DirectorViewSet,basename='director')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
