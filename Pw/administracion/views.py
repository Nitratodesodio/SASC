from django.shortcuts import render, redirect
from .forms import UsuarioCreationForm


# Create your views here.
def registrar_usuario(request):
    form = UsuarioCreationForm()
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'registro_usuario.html', {'form': form})