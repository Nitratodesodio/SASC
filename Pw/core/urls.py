from django.contrib import admin
from django.urls import path, include
from .views import  DashboardView, InformeView, AlertaView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include("autenticacion.urls")),
    path('monitoreo/', include("monitoreo.urls")),
    path('carga_planificacion/', include("carga_planificacion.urls")),
 

]
