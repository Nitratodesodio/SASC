from django.contrib import admin
from django.urls import path, include
from .views import HomeView, DashboardView, InformeView, AlertaView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include("autenticacion.urls")),
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
    path('informe/', InformeView.as_view(), name="informe"),
    path('alerta/', AlertaView.as_view(), name="alerta"),

 

]
