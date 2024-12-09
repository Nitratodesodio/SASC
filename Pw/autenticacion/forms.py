from django.contrib.auth.forms import BaseUserCreationForm
from django.forms import Select, TextInput, EmailInput, PasswordInput
from .models import Usuario, Cargo
from administracion.models import Sede

class UsuarioCreationForm(BaseUserCreationForm):

    class Meta:
        model = Usuario
        fields = ['rut', 'nombre', 'email', 'cargo', 'sede']
        labels = {
            'rut': 'Rut',
            'nombre': 'Nombre y apellidos',
            'email': 'Correo electrónico',
            'cargo': 'Cargo',
            'sede': 'Sede'

        }
        widgets = {
            'rut': TextInput(attrs={'class': 'form-control'}),
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'cargo': Select(choices=Cargo.objects.all(),attrs={'class': 'form-control'}),
            'sede': Select(choices=Sede.objects.all(),attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super(UsuarioCreationForm, self).__init__(*args, **kwargs)
        #self.fields['cargo'].queryset = Cargo.objects.all()