from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model

# Create your views here.
@login_required()
def home(request):
    usuario = request.user
    return render(request, 'home.html')


def inicio_sesion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        usuario = authenticate(request, email=email, password=password)
        if usuario:
            login(request, usuario)
            if request.user.cargo.nombre == 'Coordinación':
                return redirect('carga_planificacion')
            return redirect('home')
    return render(request, 'login.html')


def cerrar_sesion(request):
    logout(request)
    return render(request, 'login.html')

def perfil(request):
    return render(request, 'perfil.html')