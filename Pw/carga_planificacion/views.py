from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utils import cargar_clases
# Create your views here.
@login_required()
def carga_planificacion(request):
    if request.method == 'POST':
        archivo = request.FILES['file']
        cargar_clases(archivo)
    return render(request, 'carga_planificacion.html')