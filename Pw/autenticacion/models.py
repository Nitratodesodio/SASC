from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid
from administracion.models import Sede


class UsuarioManager(BaseUserManager):
    def create_user(self, rut, nombre, email, cargo, sede=None, password=None):
        if not rut:
            raise ValueError('El usuario debe tener un rut')
        if not nombre:
            raise ValueError('El usuario debe tener un nombre')
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')

        user = self.model(
            rut=rut,
            nombre=nombre,
            email=email,
            cargo=cargo,  # Ahora pasamos la instancia de Cargo
            sede=sede,  # Ahora pasamos la instancia de Sede
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, rut, nombre, email, cargo, password, sede=None):
        user = self.create_user(
            rut=rut,
            nombre=nombre,
            email=email,
            cargo=Cargo.objects.get(cod_cargo=cargo),
            sede=None,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# Create your models here.
class Cargo(models.Model):
    cod_cargo = models.SmallAutoField(primary_key=True)
    nombre = models.CharField("Cargo", max_length=40, unique=True)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        db_table = 'cargo'

    def __str__(self):
        return self.nombre

class Usuario(AbstractBaseUser):

    cod_usuario = models.AutoField(primary_key=True)
    rut = models.CharField("Rut", max_length=10, unique=True)
    nombre = models.CharField("Nombre y apellidos", max_length=40)
    email = models.EmailField("Correo electrónico", max_length=255, unique=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, db_column="cod_cargo", blank=True, null=True)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, db_column="cod_sede", blank=True, null=True)
    objects = UsuarioManager()

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['rut', 'nombre', 'cargo']

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

