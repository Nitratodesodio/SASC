from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utils import cargar_clases
# Create your views here.
@login_required()
def carga_planificacion(request):
    context = None
    if request.method == 'POST':
        archivo = request.FILES['file']
        try:
            cargar_clases(archivo)
            context = {'msje': 'Carga exitosa'}
        except:
            context = {'msje': 'Error en la carga. El archivo debe ser un Excel y debe corresponder a la planificación generada por la Intranet de coordinación docente.'}
    return render(request, 'carga_planificacion.html', context)