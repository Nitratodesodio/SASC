from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .carga_clases import carga_clases
# Create your views here.
@login_required()
def carga_planificacion(request):
    if request.method == 'POST':
        archivo = request.FILES['file']
        carga_clases(archivo)
    return render(request, 'carga_planificacion.html')