from django.urls import path
from .views import dashboard, informes

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('informes/', informes, name='informes'),
]