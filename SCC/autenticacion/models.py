from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid
from administrador.models import Sede


class UsuarioManager(BaseUserManager):
    def create_user(self, rut, nombre, usuario, cod_cargo, password=None):
        if not rut:
            raise ValueError('El usuario debe tener un rut')
        if not nombre:
            raise ValueError('El usuario debe tener un nombre')
        if not usuario:
            raise ValueError('El usuario debe tener un correo electrónico')
        if not cod_cargo:
            raise ValueError('El usuario debe tener un cargo')

        # Obtener la instancia de Cargo usando el UUID
        from autenticacion.models import Cargo
        try:
            cargo = Cargo.objects.get(cod_cargo=cod_cargo)
        except Cargo.DoesNotExist:
            raise ValueError('El cargo especificado no existe')

        user = self.model(
            rut=rut,
            nombre=nombre,
            usuario=usuario,
            cod_cargo=cargo,  # Ahora pasamos la instancia de Cargo
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, rut, nombre, usuario, cod_cargo, password):
        user = self.create_user(
            rut=rut,
            nombre=nombre,
            usuario=usuario,
            cod_cargo=cod_cargo,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
# Create your models here.
class Cargo(models.Model):
    cod_cargo = models.UUIDField(primary_key=True)
    nombre = models.CharField("Nombre del cargo",max_length=40, unique=True)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        db_table = 'cargo'


class Usuario(AbstractBaseUser):
    cod_usuario = models.UUIDField(primary_key=True, default=uuid.uuid4)
    rut = models.CharField("Rut",max_length=10, unique=True)
    nombre = models.CharField("Nombre de usuario",max_length=40)
    usuario = models.EmailField("Correo electrónico",max_length=255, unique=True)
    cod_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, db_column="cod_cargo", blank=True, null=True)
    #cod_sede = models.ForeignKey('Sede', on_delete=models.CASCADE, blank=True, null=True)
    objects = UsuarioManager()

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['rut','nombre','cod_cargo']

    def __str__(self):
        return self.nombre

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuario'

