from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utils import cargar_datos
# Create your views here.
@login_required()
def carga_data(request):
    if request.method == 'POST':
        archivo = request.FILES['file']
        cargar_datos(archivo)
    return render(request, 'carga_datos.html')