from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import UsuarioCreationForm
# Create your views here.
@login_required()
def home(request):
    if request.user.cargo.nombre == 'Coordinación':
        return redirect('carga_planificacion')
    return redirect('perfil')


def inicio_sesion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        usuario = authenticate(request, email=email, password=password)
        if usuario:
            login(request, usuario)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'login.html')


def cerrar_sesion(request):
    logout(request)
    return render(request, 'login.html')

def perfil(request):
    #Aquí cambiará el contexto adicional al perfil según el cargo del usuario
    return render(request, 'perfil.html')

def registrar_usuario(request):
    form = UsuarioCreationForm()
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'registro_usuario.html', {'form': form})