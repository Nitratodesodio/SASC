
from django.urls import path
from .views import home, inicio_sesion, cerrar_sesion, perfil, registrar_usuario
from django.conf import settings # new
from  django.conf.urls.static import static #new

urlpatterns = [

    path('',home, name="home"),
    path('login/',inicio_sesion, name="inicio_sesion"),
    path('logout/',cerrar_sesion, name="cerrar_sesion"),
    path('perfil/',perfil, name="perfil"),
    path('administracion/signin/', registrar_usuario, name="registrar"),
]
