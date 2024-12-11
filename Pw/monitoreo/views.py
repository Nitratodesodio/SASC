from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from administracion.models import Controlador,Sala, SalaTipoError, Lectura,Sensor,EstadoAc
from datetime import date, datetime, timedelta

@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required()
def informes(request):
    return render(request, 'informes.html')

@login_required()
def alertas(request):
    alertas = SalaTipoError.objects.all().order_by('-fecha')
    context = {
        'alertas': alertas
    }
    return render(request, 'alertas.html', context)