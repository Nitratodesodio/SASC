from django.urls import path
from .views import registrar_usuario

urlpatterns = [

    path('signin/',registrar_usuario, name="registrar"),

]