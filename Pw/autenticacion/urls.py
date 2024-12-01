
from django.urls import path
from .views import home, inicio_sesion, cerrar_sesion

urlpatterns = [

    path('',home, name="home"),
    path('login/',inicio_sesion, name="inicio_sesion"),
    path('logout/',cerrar_sesion, name="cerrar_sesion"),
]
