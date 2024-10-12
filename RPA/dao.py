from dto import *
class CargoDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, cargo):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO cargo (nombre) VALUES (%s) RETURNING cod_cargo", (cargo.nombre,))
        cargo.cod_cargo = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_cargo):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_cargo, nombre FROM cargo WHERE cod_cargo = %s", (cod_cargo,))
        row = cursor.fetchone()
        if row:
            return CargoDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_cargo, nombre FROM cargo")
        rows = cursor.fetchall()
        return [CargoDTO(*row) for row in rows]

    def update(self, cargo):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE cargo SET nombre = %s WHERE cod_cargo = %s", (cargo.nombre, cargo.cod_cargo))
        self.connection.commit()

    def delete(self, cod_cargo):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM cargo WHERE cod_cargo = %s", (cod_cargo,))
        self.connection.commit()


class ZonaDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, zona):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO zona (nombre) VALUES (%s) RETURNING cod_zona", (zona.nombre,))
        zona.cod_zona = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_zona):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_zona, nombre FROM zona WHERE cod_zona = %s", (cod_zona,))
        row = cursor.fetchone()
        if row:
            return ZonaDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_zona, nombre FROM zona")
        rows = cursor.fetchall()
        return [ZonaDTO(*row) for row in rows]

    def update(self, zona):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE zona SET nombre = %s WHERE cod_zona = %s", (zona.nombre, zona.cod_zona))
        self.connection.commit()

    def delete(self, cod_zona):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM zona WHERE cod_zona = %s", (cod_zona,))
        self.connection.commit()


class CiudadDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, ciudad):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO ciudad (nombre, cod_zona) VALUES (%s, %s) RETURNING cod_ciudad", 
                        (ciudad.nombre, ciudad.cod_zona))
        ciudad.cod_ciudad = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_ciudad):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_ciudad, nombre, cod_zona FROM ciudad WHERE cod_ciudad = %s", (cod_ciudad,))
        row = cursor.fetchone()
        if row:
            return CiudadDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_ciudad, nombre, cod_zona FROM ciudad")
        rows = cursor.fetchall()
        return [CiudadDTO(*row) for row in rows]

    def update(self, ciudad):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE ciudad SET nombre = %s, cod_zona = %s WHERE cod_ciudad = %s", 
                        (ciudad.nombre, ciudad.cod_zona, ciudad.cod_ciudad))
        self.connection.commit()

    def delete(self, cod_ciudad):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM ciudad WHERE cod_ciudad = %s", (cod_ciudad,))
        self.connection.commit()


class ComunaDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, comuna):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO comuna (nombre, cod_ciudad) VALUES (%s, %s) RETURNING cod_comuna", 
                        (comuna.nombre, comuna.cod_ciudad))
        comuna.cod_comuna = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_comuna):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_comuna, nombre, cod_ciudad FROM comuna WHERE cod_comuna = %s", (cod_comuna,))
        row = cursor.fetchone()
        if row:
            return ComunaDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_comuna, nombre, cod_ciudad FROM comuna")
        rows = cursor.fetchall()
        return [ComunaDTO(*row) for row in rows]

    def update(self, comuna):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE comuna SET nombre = %s, cod_ciudad = %s WHERE cod_comuna = %s", 
                        (comuna.nombre, comuna.cod_ciudad, comuna.cod_comuna))
        self.connection.commit()

    def delete(self, cod_comuna):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM comuna WHERE cod_comuna = %s", (cod_comuna,))
        self.connection.commit()


class ClimaDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, clima):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO clima (fecha_hora, temperatura, humedad, cod_comuna) VALUES (%s, %s, %s, %s) RETURNING cod_clima", 
                        (clima.fecha_hora, clima.temperatura, clima.humedad, clima.cod_comuna))
        clima.cod_clima = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_clima):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_clima, fecha_hora, temperatura, humedad, cod_comuna FROM clima WHERE cod_clima = %s", (cod_clima,))
        row = cursor.fetchone()
        if row:
            return ClimaDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_clima, fecha_hora, temperatura, humedad, cod_comuna FROM clima")
        rows = cursor.fetchall()
        return [ClimaDTO(*row) for row in rows]

    def update(self, clima):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE clima SET fecha_hora = %s, temperatura = %s, humedad = %s, cod_comuna = %s WHERE cod_clima = %s", 
                        (clima.fecha_hora, clima.temperatura, clima.humedad, clima.cod_comuna, clima.cod_clima))
        self.connection.commit()

    def delete(self, cod_clima):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM clima WHERE cod_clima = %s", (cod_clima,))
        self.connection.commit()


class SedeDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, sede):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO sede (nombre, cod_zona, cod_ciudad, cod_comuna) VALUES (%s, %s, %s, %s) RETURNING cod_sede", 
                        (sede.nombre, sede.cod_zona, sede.cod_ciudad, sede.cod_comuna))
        sede.cod_sede = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_sede):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_sede, nombre, cod_zona, cod_ciudad, cod_comuna FROM sede WHERE cod_sede = %s", (cod_sede,))
        row = cursor.fetchone()
        if row:
            return SedeDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_sede, nombre, cod_zona, cod_ciudad, cod_comuna FROM sede")
        rows = cursor.fetchall()
        return [SedeDTO(*row) for row in rows]

    def update(self, sede):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE sede SET nombre = %s, cod_zona = %s, cod_ciudad = %s, cod_comuna = %s WHERE cod_sede = %s", 
                        (sede.nombre, sede.cod_zona, sede.cod_ciudad, sede.cod_comuna, sede.cod_sede))
        self.connection.commit()

    def delete(self, cod_sede):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM sede WHERE cod_sede = %s", (cod_sede,))
        self.connection.commit()


class EdificioDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, edificio):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO edificio (nombre, cod_sede) VALUES (%s, %s) RETURNING cod_edificio", 
                        (edificio.nombre, edificio.cod_sede))
        edificio.cod_edificio = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_edificio):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_edificio, nombre, cod_sede FROM edificio WHERE cod_edificio = %s", (cod_edificio,))
        row = cursor.fetchone()
        if row:
            return EdificioDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_edificio, nombre, cod_sede FROM edificio")
        rows = cursor.fetchall()
        return [EdificioDTO(*row) for row in rows]

    def update(self, edificio):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE edificio SET nombre = %s, cod_sede = %s WHERE cod_edificio = %s", 
                        (edificio.nombre, edificio.cod_sede, edificio.cod_edificio))
        self.connection.commit()

    def delete(self, cod_edificio):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM edificio WHERE cod_edificio = %s", (cod_edificio,))
        self.connection.commit()


class UsuarioDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, usuario):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO usuario (rut, nombre, usuario, password, cod_cargo, cod_sede) VALUES (%s, %s, %s, %s, %s, %s) RETURNING cod_usuario", 
                        (usuario.rut, usuario.nombre, usuario.usuario, usuario.password, usuario.cod_cargo, usuario.cod_sede))
        usuario.cod_usuario = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_usuario):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_usuario, rut, nombre, usuario, password, cod_cargo, cod_sede FROM usuario WHERE cod_usuario = %s", (cod_usuario,))
        row = cursor.fetchone()
        if row:
            return UsuarioDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_usuario, rut, nombre, usuario, password, cod_cargo, cod_sede FROM usuario")
        rows = cursor.fetchall()
        return [UsuarioDTO(*row) for row in rows]

    def update(self, usuario):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE usuario SET rut = %s, nombre = %s, usuario = %s, password = %s, cod_cargo = %s, cod_sede = %s WHERE cod_usuario = %s", 
                        (usuario.rut, usuario.nombre, usuario.usuario, usuario.password, usuario.cod_cargo, usuario.cod_sede, usuario.cod_usuario))
        self.connection.commit()

    def delete(self, cod_usuario):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM usuario WHERE cod_usuario = %s", (cod_usuario,))
        self.connection.commit()


class TipoSensorDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, tipo_sensor):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO tipo_sensor (nombre) VALUES (%s) RETURNING cod_tipo_sensor", 
                        (tipo_sensor.nombre,))
        tipo_sensor.cod_tipo_sensor = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_tipo_sensor):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_tipo_sensor, nombre FROM tipo_sensor WHERE cod_tipo_sensor = %s", (cod_tipo_sensor,))
        row = cursor.fetchone()
        if row:
            return TipoSensorDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_tipo_sensor, nombre FROM tipo_sensor")
        rows = cursor.fetchall()
        return [TipoSensorDTO(*row) for row in rows]

    def update(self, tipo_sensor):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE tipo_sensor SET nombre = %s WHERE cod_tipo_sensor = %s", 
                        (tipo_sensor.nombre, tipo_sensor.cod_tipo_sensor))
        self.connection.commit()

    def delete(self, cod_tipo_sensor):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM tipo_sensor WHERE cod_tipo_sensor = %s", (cod_tipo_sensor,))
        self.connection.commit()


class SensorDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, sensor):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO sensor (cod_tipo_sensor) VALUES (%s) RETURNING cod_sensor", (sensor.cod_tipo_sensor,))
        sensor.cod_sensor = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_sensor):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_sensor, cod_tipo_sensor FROM sensor WHERE cod_sensor = %s", (cod_sensor,))
        row = cursor.fetchone()
        if row:
            return SensorDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_sensor, cod_tipo_sensor FROM sensor")
        rows = cursor.fetchall()
        return [SensorDTO(*row) for row in rows]

    def update(self, sensor):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE sensor SET cod_tipo_sensor = %s WHERE cod_sensor = %s", 
                       (sensor.cod_tipo_sensor, sensor.cod_sensor))
        self.connection.commit()

    def delete(self, cod_sensor):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM sensor WHERE cod_sensor = %s", (cod_sensor,))
        self.connection.commit()


class ControladorDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, controlador):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO controlador (mac, cod_sensor) VALUES (%s, %s) RETURNING cod_controlador", 
                       (controlador.mac, controlador.cod_sensor))
        controlador.cod_controlador = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_controlador):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_controlador, mac, cod_sensor FROM controlador WHERE cod_controlador = %s", (cod_controlador,))
        row = cursor.fetchone()
        if row:
            return ControladorDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_controlador, mac, cod_sensor FROM controlador")
        rows = cursor.fetchall()
        return [ControladorDTO(*row) for row in rows]

    def update(self, controlador):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE controlador SET mac = %s, cod_sensor = %s WHERE cod_controlador = %s", 
                       (controlador.mac, controlador.cod_sensor, controlador.cod_controlador))
        self.connection.commit()

    def delete(self, cod_controlador):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM controlador WHERE cod_controlador = %s", (cod_controlador,))
        self.connection.commit()


class LecturaSensorDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, lectura_sensor):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO lectura_sensor (cod_sensor, fecha_hora, temperatura, humedad, ruido, presencia, co2) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING cod_lectura",
            (lectura_sensor.cod_sensor, lectura_sensor.fecha_hora, lectura_sensor.temperatura, 
             lectura_sensor.humedad, lectura_sensor.ruido, lectura_sensor.presencia, lectura_sensor.co2)
        )
        lectura_sensor.cod_lectura = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_lectura):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_lectura, cod_sensor, fecha_hora, temperatura, humedad, ruido, presencia, co2 "
                       "FROM lectura_sensor WHERE cod_lectura = %s", (cod_lectura,))
        row = cursor.fetchone()
        if row:
            return LecturaSensorDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_lectura, cod_sensor, fecha_hora, temperatura, humedad, ruido, presencia, co2 "
                       "FROM lectura_sensor")
        rows = cursor.fetchall()
        return [LecturaSensorDTO(*row) for row in rows]

    def update(self, lectura_sensor):
        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE lectura_sensor SET cod_sensor = %s, fecha_hora = %s, temperatura = %s, "
            "humedad = %s, ruido = %s, presencia = %s, co2 = %s WHERE cod_lectura = %s",
            (lectura_sensor.cod_sensor, lectura_sensor.fecha_hora, lectura_sensor.temperatura, 
             lectura_sensor.humedad, lectura_sensor.ruido, lectura_sensor.presencia, lectura_sensor.co2, 
             lectura_sensor.cod_lectura)
        )
        self.connection.commit()

    def delete(self, cod_lectura):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM lectura_sensor WHERE cod_lectura = %s", (cod_lectura,))
        self.connection.commit()


class SalaDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, sala):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO sala (numero, cod_edificio, cod_sede, cod_controlador, cod_cap, cod_ori, cod_vol) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING cod_sala",
            (sala.numero, sala.cod_edificio, sala.cod_sede, sala.cod_controlador, sala.cod_cap, sala.cod_ori, sala.cod_vol)
        )
        sala.cod_sala = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_sala):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_sala, numero, cod_edificio, cod_sede, cod_controlador, cod_cap, cod_ori, cod_vol "
                       "FROM sala WHERE cod_sala = %s", (cod_sala,))
        row = cursor.fetchone()
        if row:
            return SalaDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_sala, numero, cod_edificio, cod_sede, cod_controlador, cod_cap, cod_ori, cod_vol FROM sala")
        rows = cursor.fetchall()
        return [SalaDTO(*row) for row in rows]

    def update(self, sala):
        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE sala SET numero = %s, cod_edificio = %s, cod_sede = %s, cod_controlador = %s, cod_cap = %s, cod_ori = %s, cod_vol = %s "
            "WHERE cod_sala = %s",
            (sala.numero, sala.cod_edificio, sala.cod_sede, sala.cod_controlador, sala.cod_cap, sala.cod_ori, sala.cod_vol, sala.cod_sala)
        )
        self.connection.commit()

    def delete(self, cod_sala):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM sala WHERE cod_sala = %s", (cod_sala,))
        self.connection.commit()


class VolumenDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, volumen):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO volumen (volumen) VALUES (%s) RETURNING cod_vol", (volumen.volumen,))
        volumen.cod_vol = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_vol):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_vol, volumen FROM volumen WHERE cod_vol = %s", (cod_vol,))
        row = cursor.fetchone()
        if row:
            return VolumenDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_vol, volumen FROM volumen")
        rows = cursor.fetchall()
        return [VolumenDTO(*row) for row in rows]

    def update(self, volumen):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE volumen SET volumen = %s WHERE cod_vol = %s", (volumen.volumen, volumen.cod_vol))
        self.connection.commit()

    def delete(self, cod_vol):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM volumen WHERE cod_vol = %s", (cod_vol,))
        self.connection.commit()


class OrientacionDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, orientacion):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO orientacion (orientacion) VALUES (%s) RETURNING cod_ori", (orientacion.orientacion,))
        orientacion.cod_ori = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_ori):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_ori, orientacion FROM orientacion WHERE cod_ori = %s", (cod_ori,))
        row = cursor.fetchone()
        if row:
            return OrientacionDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_ori, orientacion FROM orientacion")
        rows = cursor.fetchall()
        return [OrientacionDTO(*row) for row in rows]

    def update(self, orientacion):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE orientacion SET orientacion = %s WHERE cod_ori = %s", (orientacion.orientacion, orientacion.cod_ori))
        self.connection.commit()

    def delete(self, cod_ori):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM orientacion WHERE cod_ori = %s", (cod_ori,))
        self.connection.commit()


class CapacidadDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, capacidad):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO capacidad (cupo_estandar, cupo_permitido) VALUES (%s, %s) RETURNING cod_cap", 
                       (capacidad.cupo_estandar, capacidad.cupo_permitido))
        capacidad.cod_cap = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_cap):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_cap, cupo_estandar, cupo_permitido FROM capacidad WHERE cod_cap = %s", (cod_cap,))
        row = cursor.fetchone()
        if row:
            return CapacidadDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_cap, cupo_estandar, cupo_permitido FROM capacidad")
        rows = cursor.fetchall()
        return [CapacidadDTO(*row) for row in rows]

    def update(self, capacidad):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE capacidad SET cupo_estandar = %s, cupo_permitido = %s WHERE cod_cap = %s", 
                       (capacidad.cupo_estandar, capacidad.cupo_permitido, capacidad.cod_cap))
        self.connection.commit()

    def delete(self, cod_cap):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM capacidad WHERE cod_cap = %s", (cod_cap,))
        self.connection.commit()


class TipoAcDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, tipo_ac):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO tipo_ac (nombre) VALUES (%s) RETURNING cod_tipo", (tipo_ac.nombre,))
        tipo_ac.cod_tipo = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_tipo):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_tipo, nombre FROM tipo_ac WHERE cod_tipo = %s", (cod_tipo,))
        row = cursor.fetchone()
        if row:
            return TipoAcDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_tipo, nombre FROM tipo_ac")
        rows = cursor.fetchall()
        return [TipoAcDTO(*row) for row in rows]

    def update(self, tipo_ac):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE tipo_ac SET nombre = %s WHERE cod_tipo = %s", 
                       (tipo_ac.nombre, tipo_ac.cod_tipo))
        self.connection.commit()

    def delete(self, cod_tipo):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM tipo_ac WHERE cod_tipo = %s", (cod_tipo,))
        self.connection.commit()


class MarcaAcDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, marca_ac):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO marca_ac (nombre) VALUES (%s) RETURNING cod_marca", (marca_ac.nombre,))
        marca_ac.cod_marca = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_marca):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_marca, nombre FROM marca_ac WHERE cod_marca = %s", (cod_marca,))
        row = cursor.fetchone()
        if row:
            return MarcaAcDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_marca, nombre FROM marca_ac")
        rows = cursor.fetchall()
        return [MarcaAcDTO(*row) for row in rows]

    def update(self, marca_ac):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE marca_ac SET nombre = %s WHERE cod_marca = %s", 
                       (marca_ac.nombre, marca_ac.cod_marca))
        self.connection.commit()

    def delete(self, cod_marca):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM marca_ac WHERE cod_marca = %s", (cod_marca,))
        self.connection.commit()


class ModeloAcDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, modelo_ac):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO modelo_ac (modelo) VALUES (%s) RETURNING cod_modelo", (modelo_ac.modelo,))
        modelo_ac.cod_modelo = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_modelo):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_modelo, modelo FROM modelo_ac WHERE cod_modelo = %s", (cod_modelo,))
        row = cursor.fetchone()
        if row:
            return ModeloAcDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_modelo, modelo FROM modelo_ac")
        rows = cursor.fetchall()
        return [ModeloAcDTO(*row) for row in rows]

    def update(self, modelo_ac):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE modelo_ac SET modelo = %s WHERE cod_modelo = %s", 
                       (modelo_ac.modelo, modelo_ac.cod_modelo))
        self.connection.commit()

    def delete(self, cod_modelo):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM modelo_ac WHERE cod_modelo = %s", (cod_modelo,))
        self.connection.commit()


class BtuTipoDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, btu_tipo):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO btu_tipo (tipo) VALUES (%s) RETURNING cod_btu_tipo", (btu_tipo.tipo,))
        btu_tipo.cod_btu_tipo = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_btu_tipo):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_btu_tipo, tipo FROM btu_tipo WHERE cod_btu_tipo = %s", (cod_btu_tipo,))
        row = cursor.fetchone()
        if row:
            return BtuTipoDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_btu_tipo, tipo FROM btu_tipo")
        rows = cursor.fetchall()
        return [BtuTipoDTO(*row) for row in rows]

    def update(self, btu_tipo):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE btu_tipo SET tipo = %s WHERE cod_btu_tipo = %s", 
                       (btu_tipo.tipo, btu_tipo.cod_btu_tipo))
        self.connection.commit()

    def delete(self, cod_btu_tipo):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM btu_tipo WHERE cod_btu_tipo = %s", (cod_btu_tipo,))
        self.connection.commit()


class BtuAcDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, btu_ac):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO btu_ac (valor, cod_btu_tipo) VALUES (%s, %s) RETURNING cod_btu", 
                       (btu_ac.valor, btu_ac.cod_btu_tipo))
        btu_ac.cod_btu = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_btu):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_btu, valor, cod_btu_tipo FROM btu_ac WHERE cod_btu = %s", (cod_btu,))
        row = cursor.fetchone()
        if row:
            return BtuAcDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_btu, valor, cod_btu_tipo FROM btu_ac")
        rows = cursor.fetchall()
        return [BtuAcDTO(*row) for row in rows]

    def update(self, btu_ac):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE btu_ac SET valor = %s, cod_btu_tipo = %s WHERE cod_btu = %s", 
                       (btu_ac.valor, btu_ac.cod_btu_tipo, btu_ac.cod_btu))
        self.connection.commit()

    def delete(self, cod_btu):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM btu_ac WHERE cod_btu = %s", (cod_btu,))
        self.connection.commit()


class AcDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, ac):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO ac (cod_sala, cod_tipo, cod_marca, cod_modelo, cod_btu) "
                       "VALUES (%s, %s, %s, %s, %s) RETURNING cod_ac", 
                       (ac.cod_sala, ac.cod_tipo, ac.cod_marca, ac.cod_modelo, ac.cod_btu))
        ac.cod_ac = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_ac):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_ac, cod_sala, cod_tipo, cod_marca, cod_modelo, cod_btu FROM ac WHERE cod_ac = %s", (cod_ac,))
        row = cursor.fetchone()
        if row:
            return AcDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_ac, cod_sala, cod_tipo, cod_marca, cod_modelo, cod_btu FROM ac")
        rows = cursor.fetchall()
        return [AcDTO(*row) for row in rows]

    def update(self, ac):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE ac SET cod_sala = %s, cod_tipo = %s, cod_marca = %s, cod_modelo = %s, cod_btu = %s "
                       "WHERE cod_ac = %s", 
                       (ac.cod_sala, ac.cod_tipo, ac.cod_marca, ac.cod_modelo, ac.cod_btu, ac.cod_ac))
        self.connection.commit()

    def delete(self, cod_ac):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM ac WHERE cod_ac = %s", (cod_ac,))
        self.connection.commit()


class ModalidadDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, modalidad):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO modalidad (modalidad) VALUES (%s) RETURNING cod_mod", (modalidad.modalidad,))
        modalidad.cod_mod = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_mod):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_mod, modalidad FROM modalidad WHERE cod_mod = %s", (cod_mod,))
        row = cursor.fetchone()
        if row:
            return ModalidadDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_mod, modalidad FROM modalidad")
        rows = cursor.fetchall()
        return [ModalidadDTO(*row) for row in rows]

    def update(self, modalidad):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE modalidad SET modalidad = %s WHERE cod_mod = %s", 
                       (modalidad.modalidad, modalidad.cod_mod))
        self.connection.commit()

    def delete(self, cod_mod):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM modalidad WHERE cod_mod = %s", (cod_mod,))
        self.connection.commit()


class SeccionDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, seccion):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO seccion (seccion) VALUES (%s) RETURNING cod_sec", (seccion.seccion,))
        seccion.cod_sec = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_sec):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_sec, seccion FROM seccion WHERE cod_sec = %s", (cod_sec,))
        row = cursor.fetchone()
        if row:
            return SeccionDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_sec, seccion FROM seccion")
        rows = cursor.fetchall()
        return [SeccionDTO(*row) for row in rows]

    def update(self, seccion):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE seccion SET seccion = %s WHERE cod_sec = %s", 
                       (seccion.seccion, seccion.cod_sec))
        self.connection.commit()

    def delete(self, cod_sec):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM seccion WHERE cod_sec = %s", (cod_sec,))
        self.connection.commit()


class SemestreDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, semestre):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO semestre (semestre) VALUES (%s) RETURNING cod_sem", (semestre.semestre,))
        semestre.cod_sem = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_sem):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_sem, semestre FROM semestre WHERE cod_sem = %s", (cod_sem,))
        row = cursor.fetchone()
        if row:
            return SemestreDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_sem, semestre FROM semestre")
        rows = cursor.fetchall()
        return [SemestreDTO(*row) for row in rows]

    def update(self, semestre):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE semestre SET semestre = %s WHERE cod_sem = %s", 
                       (semestre.semestre, semestre.cod_sem))
        self.connection.commit()

    def delete(self, cod_sem):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM semestre WHERE cod_sem = %s", (cod_sem,))
        self.connection.commit()


class AsignaturaDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, asignatura):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO asignatura (identificador, nombre, cod_mod, cod_sem) "
                       "VALUES (%s, %s, %s, %s) RETURNING cod_asig", 
                       (asignatura.identificador, asignatura.nombre, asignatura.cod_mod, asignatura.cod_sem))
        asignatura.cod_asig = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_asig):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_asig, identificador, nombre, cod_mod, cod_sem FROM asignatura WHERE cod_asig = %s", (cod_asig,))
        row = cursor.fetchone()
        if row:
            return AsignaturaDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_asig, identificador, nombre, cod_mod, cod_sem FROM asignatura")
        rows = cursor.fetchall()
        return [AsignaturaDTO(*row) for row in rows]

    def update(self, asignatura):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE asignatura SET identificador = %s, nombre = %s, cod_mod = %s, cod_sem = %s "
                       "WHERE cod_asig = %s", 
                       (asignatura.identificador, asignatura.nombre, asignatura.cod_mod, asignatura.cod_sem, asignatura.cod_asig))
        self.connection.commit()

    def delete(self, cod_asig):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM asignatura WHERE cod_asig = %s", (cod_asig,))
        self.connection.commit()


class DocenteDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, docente):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO docente (rut, nombre, primer_apellido, segundo_apellido) "
                       "VALUES (%s, %s, %s, %s) RETURNING cod_docente", 
                       (docente.rut, docente.nombre, docente.primer_apellido, docente.segundo_apellido))
        docente.cod_docente = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_docente):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_docente, rut, nombre, primer_apellido, segundo_apellido FROM docente WHERE cod_docente = %s", (cod_docente,))
        row = cursor.fetchone()
        if row:
            return DocenteDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_docente, rut, nombre, primer_apellido, segundo_apellido FROM docente")
        rows = cursor.fetchall()
        return [DocenteDTO(*row) for row in rows]

    def update(self, docente):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE docente SET rut = %s, nombre = %s, primer_apellido = %s, segundo_apellido = %s "
                       "WHERE cod_docente = %s", 
                       (docente.rut, docente.nombre, docente.primer_apellido, docente.segundo_apellido, docente.cod_docente))
        self.connection.commit()

    def delete(self, cod_docente):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM docente WHERE cod_docente = %s", (cod_docente,))
        self.connection.commit()


class DocenteAsignaturaSeccionDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, docente_asignatura_seccion):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO docente_asignatura_seccion (cod_sec, cod_docente, cod_asig) "
                       "VALUES (%s, %s, %s) RETURNING cod_doc_asig_sec", 
                       (docente_asignatura_seccion.cod_sec, docente_asignatura_seccion.cod_docente, docente_asignatura_seccion.cod_asig))
        docente_asignatura_seccion.cod_doc_asig_sec = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_doc_asig_sec):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_doc_asig_sec, cod_sec, cod_docente, cod_asig FROM docente_asignatura_seccion WHERE cod_doc_asig_sec = %s", (cod_doc_asig_sec,))
        row = cursor.fetchone()
        if row:
            return DocenteAsignaturaSeccionDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_doc_asig_sec, cod_sec, cod_docente, cod_asig FROM docente_asignatura_seccion")
        rows = cursor.fetchall()
        return [DocenteAsignaturaSeccionDTO(*row) for row in rows]

    def update(self, docente_asignatura_seccion):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE docente_asignatura_seccion SET cod_sec = %s, cod_docente = %s, cod_asig = %s "
                       "WHERE cod_doc_asig_sec = %s", 
                       (docente_asignatura_seccion.cod_sec, docente_asignatura_seccion.cod_docente, docente_asignatura_seccion.cod_asig, 
                        docente_asignatura_seccion.cod_doc_asig_sec))
        self.connection.commit()

    def delete(self, cod_doc_asig_sec):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM docente_asignatura_seccion WHERE cod_doc_asig_sec = %s", (cod_doc_asig_sec,))
        self.connection.commit()


class BloqueHorarioDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, bloque_horario):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO bloque_horario (bloque, hora_inicio, hora_fin) VALUES (%s, %s, %s) RETURNING bloque", 
                       (bloque_horario.bloque, bloque_horario.hora_inicio, bloque_horario.hora_fin))
        bloque_horario.bloque = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, bloque):
        cursor = self.connection.cursor()
        cursor.execute("SELECT bloque, hora_inicio, hora_fin FROM bloque_horario WHERE bloque = %s", (bloque,))
        row = cursor.fetchone()
        if row:
            return BloqueHorarioDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT bloque, hora_inicio, hora_fin FROM bloque_horario")
        rows = cursor.fetchall()
        return [BloqueHorarioDTO(*row) for row in rows]

    def update(self, bloque_horario):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE bloque_horario SET hora_inicio = %s, hora_fin = %s WHERE bloque = %s", 
                       (bloque_horario.hora_inicio, bloque_horario.hora_fin, bloque_horario.bloque))
        self.connection.commit()

    def delete(self, bloque):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM bloque_horario WHERE bloque = %s", (bloque,))
        self.connection.commit()


class ClaseDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, clase):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO clase (cod_asig, cod_sala, sala_real, bloque) "
                       "VALUES (%s, %s, %s, %s) RETURNING cod_clase", 
                       (clase.cod_asig, clase.cod_sala, clase.sala_real, clase.bloque))
        clase.cod_clase = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_clase):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_clase, cod_asig, cod_sala, sala_real, bloque FROM clase WHERE cod_clase = %s", (cod_clase,))
        row = cursor.fetchone()
        if row:
            return ClaseDTO(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_clase, cod_asig, cod_sala, sala_real, bloque FROM clase")
        rows = cursor.fetchall()
        return [ClaseDTO(*row) for row in rows]

    def update(self, clase):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE clase SET cod_asig = %s, cod_sala = %s, sala_real = %s, bloque = %s WHERE cod_clase = %s", 
                       (clase.cod_asig, clase.cod_sala, clase.sala_real, clase.bloque, clase.cod_clase))
        self.connection.commit()

    def delete(self, cod_clase):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM clase WHERE cod_clase = %s", (cod_clase,))
        self.connection.commit()
