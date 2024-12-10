from django.urls import path
from .views import carga_data

urlpatterns = [

    path('carga_data/',carga_data, name="carga_data"),

]