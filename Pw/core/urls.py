from django.contrib import admin
from django.urls import path, include
from .views import  DashboardView, InformeView, AlertaView
from django.conf import settings # new
from  django.conf.urls.static import static #new

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',include("autenticacion.urls")),
    path('monitoreo/', include("monitoreo.urls")),
    path('carga_planificacion/', include("carga_planificacion.urls")),
    path('administracion/', include("administracion.urls")),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)