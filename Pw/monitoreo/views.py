from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required()
def informes(request):
    return render(request, 'informes.html')

@login_required()
def alertas(request):
    return render(request, 'alertas.html')