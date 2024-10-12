class CargoDTO:
    def __init__(self, cod_cargo, nombre):
        self.cod_cargo = cod_cargo
        self.nombre = nombre


class ZonaDTO:
    def __init__(self, cod_zona, nombre):
        self.cod_zona = cod_zona
        self.nombre = nombre


class CiudadDTO:
    def __init__(self, cod_ciudad, nombre, cod_zona):
        self.cod_ciudad = cod_ciudad
        self.nombre = nombre
        self.cod_zona = cod_zona


class ComunaDTO:
    def __init__(self, cod_comuna, nombre, cod_ciudad):
        self.cod_comuna = cod_comuna
        self.nombre = nombre
        self.cod_ciudad = cod_ciudad


class ClimaDTO:
    def __init__(self, cod_clima, fecha_hora, temperatura, humedad, cod_comuna):
        self.cod_clima = cod_clima
        self.fecha_hora = fecha_hora
        self.temperatura = temperatura
        self.humedad = humedad
        self.cod_comuna = cod_comuna


class SedeDTO:
    def __init__(self, cod_sede, nombre, cod_zona, cod_ciudad, cod_comuna):
        self.cod_sede = cod_sede
        self.nombre = nombre
        self.cod_zona = cod_zona
        self.cod_ciudad = cod_ciudad
        self.cod_comuna = cod_comuna


class EdificioDTO:
    def __init__(self, cod_edificio, nombre, cod_sede):
        self.cod_edificio = cod_edificio
        self.nombre = nombre
        self.cod_sede = cod_sede


class UsuarioDTO:
    def __init__(self, cod_usuario, rut, nombre, usuario, password, cod_cargo, cod_sede):
        self.cod_usuario = cod_usuario
        self.rut = rut
        self.nombre = nombre
        self.usuario = usuario
        self.password = password
        self.cod_cargo = cod_cargo
        self.cod_sede = cod_sede


class TipoSensorDTO:
    def __init__(self, cod_tipo_sensor, nombre):
        self.cod_tipo_sensor = cod_tipo_sensor
        self.nombre = nombre


class SensorDTO:
    def __init__(self, cod_sensor, cod_tipo_sensor):
        self.cod_sensor = cod_sensor
        self.cod_tipo_sensor = cod_tipo_sensor


class ControladorDTO:
    def __init__(self, cod_controlador, mac, cod_sensor):
        self.cod_controlador = cod_controlador
        self.mac = mac
        self.cod_sensor = cod_sensor


class LecturaSensorDTO:
    def __init__(self, cod_lectura, cod_sensor, fecha_hora, temperatura, humedad, ruido, presencia, co2):
        self.cod_lectura = cod_lectura
        self.cod_sensor = cod_sensor
        self.fecha_hora = fecha_hora
        self.temperatura = temperatura
        self.humedad = humedad
        self.ruido = ruido
        self.presencia = presencia
        self.co2 = co2


class SalaDTO:
    def __init__(self, cod_sala, numero, cod_edificio, cod_sede, cod_controlador):
        self.cod_sala = cod_sala
        self.numero = numero
        self.cod_edificio = cod_edificio
        self.cod_sede = cod_sede
        self.cod_controlador = cod_controlador


class VolumenDTO:
    def __init__(self, cod_vol, volumen):
        self.cod_vol = cod_vol
        self.volumen = volumen


class SalaVolDTO:
    def __init__(self, cod_salvol, cod_sala, cod_vol):
        self.cod_salvol = cod_salvol
        self.cod_sala = cod_sala
        self.cod_vol = cod_vol


class OrientacionDTO:
    def __init__(self, cod_ori, orientacion):
        self.cod_ori = cod_ori
        self.orientacion = orientacion


class CapacidadDTO:
    def __init__(self, cod_cap, cupo_estandar, cupo_permitido):
        self.cod_cap = cod_cap
        self.cupo_estandar = cupo_estandar
        self.cupo_permitido = cupo_permitido


class SalaCapDTO:
    def __init__(self, cod_sal_cap, cod_sala, cod_cap):
        self.cod_sal_cap = cod_sal_cap
        self.cod_sala = cod_sala
        self.cod_cap = cod_cap


class TipoAcDTO:
    def __init__(self, cod_tipo, nombre):
        self.cod_tipo = cod_tipo
        self.nombre = nombre


class MarcaAcDTO:
    def __init__(self, cod_marca, nombre):
        self.cod_marca = cod_marca
        self.nombre = nombre


class ModeloAcDTO:
    def __init__(self, cod_modelo, modelo):
        self.cod_modelo = cod_modelo
        self.modelo = modelo


class BtuTipoDTO:
    def __init__(self, cod_btu_tipo, tipo):
        self.cod_btu_tipo = cod_btu_tipo
        self.tipo = tipo


class BtuAcDTO:
    def __init__(self, cod_btu, valor, cod_btu_tipo):
        self.cod_btu = cod_btu
        self.valor = valor
        self.cod_btu_tipo = cod_btu_tipo


class AcDTO:
    def __init__(self, cod_ac, cod_sala, cod_tipo, cod_marca, cod_modelo, cod_btu):
        self.cod_ac = cod_ac
        self.cod_sala = cod_sala
        self.cod_tipo = cod_tipo
        self.cod_marca = cod_marca
        self.cod_modelo = cod_modelo
        self.cod_btu = cod_btu


class ModalidadDTO:
    def __init__(self, cod_mod, modalidad):
        self.cod_mod = cod_mod
        self.modalidad = modalidad


class SeccionDTO:
    def __init__(self, cod_sec, seccion):
        self.cod_sec = cod_sec
        self.seccion = seccion


class TipoSubseccionDTO:
    def __init__(self, cod_tipo_su, nombre):
        self.cod_tipo_su = cod_tipo_su
        self.nombre = nombre


class SemestreDTO:
    def __init__(self, cod_sem, semestre):
        self.cod_sem = cod_sem
        self.semestre = semestre


class AsignaturaDTO:
    def __init__(self, cod_asig, identificador, nombre, cod_mod, cod_sem):
        self.cod_asig = cod_asig
        self.identificador = identificador
        self.nombre = nombre
        self.cod_mod = cod_mod
        self.cod_sem = cod_sem


class DocenteDTO:
    def __init__(self, cod_docente, rut, nombre, primer_apellido, segundo_apellido):
        self.cod_docente = cod_docente
        self.rut = rut
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido


class DocenteAsignaturaSeccionDTO:
    def __init__(self, cod_doc_asig_sec, cod_sec, cod_docente, cod_asig):
        self.cod_doc_asig_sec = cod_doc_asig_sec
        self.cod_sec = cod_sec
        self.cod_docente = cod_docente
        self.cod_asig = cod_asig


class BloqueHorarioDTO:
    def __init__(self, bloque, hora_inicio, hora_fin):
        self.bloque = bloque
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin


class ClaseDTO:
    def __init__(self, cod_clase, cod_asig, cod_sala, sala_real, bloque):
        self.cod_clase = cod_clase
        self.cod_asig = cod_asig
        self.cod_sala = cod_sala
        self.sala_real = sala_real
        self.bloque = bloque
