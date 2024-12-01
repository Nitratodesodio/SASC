from django.urls import path
from .views import carga_planificacion
urlpatterns = [
    path('',carga_planificacion, name="carga_planificacion"),
]