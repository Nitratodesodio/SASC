from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utils import cargar_datos
# Create your views here.
@login_required()
def carga_data(request):
    context = None
    if request.method == 'POST':
        archivo = request.FILES['file']
        try:
            cargar_datos(archivo)
            context = {'msje': 'Datos cargados correctamente'}
        except:
            context = {'msje': 'Error al cargar los datos. El archivo debe ser un archivo de Excel y con el formato generado por la intranet de coordinación docente.'}
    return render(request, 'carga_datos.html', context)