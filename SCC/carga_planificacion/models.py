from django.db import models
from administrador.models import Sala

# Create your models here.
class Modalidad(models.Model):
    cod_mod = models.UUIDField(primary_key=True)
    modalidad = models.CharField(unique=True, max_length=25)

    class Meta:
        managed = False
        db_table = 'modalidad'


class Seccion(models.Model):
    cod_sec = models.UUIDField(primary_key=True)
    seccion = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'seccion'


class Semestre(models.Model):
    cod_sem = models.UUIDField(primary_key=True)
    semestre = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'semestre'


class Asignatura(models.Model):
    cod_asig = models.UUIDField(primary_key=True)
    identificador = models.CharField(unique=True, max_length=30)
    nombre = models.CharField(max_length=100)
    cod_mod = models.ForeignKey(Modalidad, models.DO_NOTHING, db_column='cod_mod', blank=True, null=True)
    cod_sem = models.ForeignKey(Semestre, models.DO_NOTHING, db_column='cod_sem', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asignatura'


class Docente(models.Model):
    cod_docente = models.UUIDField(primary_key=True)
    rut = models.CharField(unique=True, max_length=10)
    nombre = models.CharField(max_length=30)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'docente'


class DocenteAsignaturaSeccion(models.Model):
    cod_doc_asig_sec = models.UUIDField(primary_key=True)
    cod_sec = models.ForeignKey(Seccion, models.DO_NOTHING, db_column='cod_sec', blank=True, null=True)
    cod_docente = models.ForeignKey(Docente, models.DO_NOTHING, db_column='cod_docente', blank=True, null=True)
    cod_asig = models.ForeignKey(Asignatura, models.DO_NOTHING, db_column='cod_asig', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'docente_asignatura_seccion'


class BloqueHorario(models.Model):
    bloque = models.AutoField(primary_key=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        managed = False
        db_table = 'bloque_horario'


class Clase(models.Model):
    cod_clase = models.UUIDField(primary_key=True)
    cod_doc_asig_sec = models.ForeignKey(DocenteAsignaturaSeccion, models.DO_NOTHING, db_column='cod_doc_asig_sec',
                                         blank=True, null=True)
    cod_sala = models.ForeignKey(Sala, models.DO_NOTHING, db_column='cod_sala', blank=True, null=True)
    sala_real = models.CharField(max_length=20, blank=True, null=True)
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'clase'


class BloqueClase(models.Model):
    cod_bloque_clase = models.UUIDField(primary_key=True)
    bloque = models.ForeignKey(BloqueHorario, models.DO_NOTHING, db_column='bloque')
    cod_clase = models.ForeignKey(Clase, models.DO_NOTHING, db_column='cod_clase')

    class Meta:
        managed = False
        db_table = 'bloque_clase'