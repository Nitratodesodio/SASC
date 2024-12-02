from django.urls import path
from .views import dashboard, informes, alertas

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('informes/', informes, name='informes'),
    path('alertas/', alertas, name='alertas'),
]