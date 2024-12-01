from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required()
def carga_planificacion(request):
    return render(request, 'carga_planificacion.html')