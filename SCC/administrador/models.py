# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Zona(models.Model):
    cod_zona = models.UUIDField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'zona'


class Ciudad(models.Model):
    cod_ciudad = models.UUIDField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)
    cod_zona = models.ForeignKey('Zona', models.DO_NOTHING, db_column='cod_zona', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ciudad'


class Comuna(models.Model):
    cod_comuna = models.UUIDField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=20)
    cod_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='cod_ciudad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comuna'


class Clima(models.Model):
    cod_clima = models.UUIDField(primary_key=True)
    fecha_hora = models.DateTimeField()
    temperatura = models.DecimalField(max_digits=5, decimal_places=2)
    humedad = models.DecimalField(max_digits=5, decimal_places=2)
    cod_comuna = models.ForeignKey('Comuna', models.DO_NOTHING, db_column='cod_comuna', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clima'


class Sede(models.Model):
    cod_sede = models.UUIDField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=30)
    cod_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='cod_comuna', blank=True, null=True)

    class Meta:

        db_table = 'sede'


class Edificio(models.Model):
    cod_edificio = models.UUIDField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=30)
    cod_sede = models.ForeignKey(Sede, models.DO_NOTHING, db_column='cod_sede', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edificio'


class Controlador(models.Model):
    cod_controlador = models.UUIDField(primary_key=True)
    mac = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'controlador'


class TipoSensor(models.Model):
    cod_tipo_sensor = models.UUIDField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_sensor'


class Sensor(models.Model):
    cod_sensor = models.UUIDField(primary_key=True)
    cod_tipo_sensor = models.ForeignKey(TipoSensor, models.DO_NOTHING, db_column='cod_tipo_sensor', blank=True, null=True)
    cod_controlador = models.ForeignKey(Controlador, models.DO_NOTHING, db_column='cod_controlador', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensor'


class Lectura(models.Model):
    cod_lectura = models.UUIDField(primary_key=True)
    cod_sensor = models.ForeignKey(Sensor, models.DO_NOTHING, db_column='cod_sensor', blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    fecha_hora = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lectura'


class Orientacion(models.Model):
    cod_ori = models.UUIDField(primary_key=True)
    orientacion = models.CharField(unique=True, max_length=25)

    class Meta:
        managed = False
        db_table = 'orientacion'


class Sala(models.Model):
    cod_sala = models.UUIDField(primary_key=True)
    sala = models.CharField(unique=True, max_length=25)
    capacidad = models.IntegerField(blank=True, null=True)
    cod_edificio = models.ForeignKey(Edificio, models.DO_NOTHING, db_column='cod_edificio', blank=True, null=True)
    cod_controlador = models.OneToOneField(Controlador, models.DO_NOTHING, db_column='cod_controlador', blank=True, null=True)
    volumen = models.IntegerField(blank=True, null=True)
    cod_ori = models.ForeignKey(Orientacion, models.DO_NOTHING, db_column='cod_ori', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sala'


class TipoAc(models.Model):
    cod_tipo = models.UUIDField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_ac'


class MarcaAc(models.Model):
    cod_marca = models.UUIDField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'marca_ac'


class ModeloAc(models.Model):
    cod_modelo = models.UUIDField(primary_key=True)
    modelo = models.CharField(unique=True, max_length=25)

    class Meta:
        managed = False
        db_table = 'modelo_ac'


class Ac(models.Model):
    cod_ac = models.UUIDField(primary_key=True)
    cod_sala = models.ForeignKey(Sala, models.DO_NOTHING, db_column='cod_sala', blank=True, null=True)
    cod_tipo = models.ForeignKey(TipoAc, models.DO_NOTHING, db_column='cod_tipo', blank=True, null=True)
    cod_marca = models.ForeignKey(MarcaAc, models.DO_NOTHING, db_column='cod_marca', blank=True, null=True)
    cod_modelo = models.ForeignKey(ModeloAc, models.DO_NOTHING, db_column='cod_modelo', blank=True, null=True)
    btu = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac'


class Estado(models.Model):
    cod_estado = models.UUIDField(primary_key=True)
    estado = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'estado'


class EstadoAc(models.Model):
    cod_estado_ac = models.UUIDField(primary_key=True)
    cod_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='cod_estado', blank=True, null=True)
    cod_ac = models.ForeignKey(Ac, models.DO_NOTHING, db_column='cod_ac', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_ac'
