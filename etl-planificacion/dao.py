from dto import *

class ModalidadDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, modalidad):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO modalidad (modalidad) "
                       "VALUES (%s) RETURNING cod_mod", 
                       (modalidad.modalidad,))
        modalidad.cod_mod = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_mod):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_mod, modalidad FROM modalidad WHERE cod_mod = %s", (cod_mod,))
        row = cursor.fetchone()
        if row:
            return Modalidad(*row)
        return None

    def get_id_by_modalidad(self, modalidad):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_mod FROM modalidad WHERE modalidad = %s", (modalidad,))
        row = cursor.fetchone()
        if row:
            return row[0]
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_mod, modalidad FROM modalidad")
        rows = cursor.fetchall()
        return [Modalidad(*row) for row in rows]

    def update(self, modalidad):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE modalidad SET modalidad = %s WHERE cod_mod = %s", 
                       (modalidad.modalidad, modalidad.cod_mod))
        self.connection.commit()

    def delete(self, cod_mod):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM modalidad WHERE cod_mod = %s", (cod_mod,))
        self.connection.commit()


class SemestreDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, semestre):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO semestre (semestre) "
                       "VALUES (%s) RETURNING cod_sem", 
                       (semestre.semestre,))
        semestre.cod_sem = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_sem):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_sem, semestre FROM semestre WHERE cod_sem = %s", (cod_sem,))
        row = cursor.fetchone()
        if row:
            return Semestre(*row)
        return None

    def get_id_by_semestre(self, semestre):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_sem FROM semestre WHERE semestre = %s", (semestre,))
        row = cursor.fetchone()
        if row:
            return row[0]
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_sem, semestre FROM semestre")
        rows = cursor.fetchall()
        return [Semestre(*row) for row in rows]

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
        cursor.execute("INSERT INTO asignatura (cod_mod, cod_sem, identificador, nombre) "
                       "VALUES (%s, %s, %s, %s) RETURNING cod_asig", 
                       (asignatura.cod_mod, asignatura.cod_sem, asignatura.identificador, asignatura.nombre))
        asignatura.cod_asig = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_asig):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_asig, cod_mod, cod_sem, identificador, nombre FROM asignatura WHERE cod_asig = %s", (cod_asig,))
        row = cursor.fetchone()
        if row:
            return Asignatura(*row)
        return None
    
    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_asig, cod_mod, cod_sem, identificador, nombre FROM asignatura")
        rows = cursor.fetchall()
        return [Asignatura(*row) for row in rows]
    
    def update(self, asignatura):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE asignatura SET cod_mod = %s, cod_sem = %s, identificador = %s, nombre = %s WHERE cod_asig = %s", 
                       (asignatura.cod_mod, asignatura.cod_sem, asignatura.identificador, asignatura.nombre, asignatura.cod_asig))
        self.connection.commit()

    def delete(self, cod_asig):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM asignatura WHERE cod_asig = %s", (cod_asig,))
        self.connection.commit()

    def get_id_by_identificador(self, identificador):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_asig FROM asignatura WHERE identificador = %s", (identificador,))
        row = cursor.fetchone()
        if row:
            return row[0]
        return None


class SeccionDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, seccion):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO seccion (seccion) "
                       "VALUES (%s) RETURNING cod_sec", 
                       (seccion.seccion,))
        seccion.cod_sec = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_sec):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_sec, seccion FROM seccion WHERE cod_sec = %s", (cod_sec,))
        row = cursor.fetchone()
        if row:
            return Seccion(*row)
        return None

    def get_id_by_seccion(self, seccion):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_sec FROM seccion WHERE seccion = %s", (seccion,))
        row = cursor.fetchone()
        if row:
            return row[0]
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_sec, seccion FROM seccion")
        rows = cursor.fetchall()
        return [Seccion(*row) for row in rows]

    def update(self, seccion):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE seccion SET seccion = %s WHERE cod_sec = %s", 
                       (seccion.seccion, seccion.cod_sec))
        self.connection.commit()

    def delete(self, cod_sec):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM seccion WHERE cod_sec = %s", (cod_sec,))
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
            return Docente(*row)
        return None

    def get_id_by_rut(self, rut):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_docente FROM docente WHERE rut = %s", (rut,))
        row = cursor.fetchone()
        if row:
            return row[0]
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_docente, rut, nombre, primer_apellido, segundo_apellido FROM docente")
        rows = cursor.fetchall()
        return [Docente(*row) for row in rows]

    def update(self, docente):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE docente SET rut = %s, nombre = %s, primer_apellido = %s, segundo_apellido = %s WHERE cod_docente = %s", 
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
        cursor.execute("INSERT INTO docente_asignatura_seccion (cod_docente, cod_asig, cod_sec) "
                       "VALUES (%s, %s, %s) RETURNING cod_doc_asig_sec", 
                       (docente_asignatura_seccion.cod_docente, docente_asignatura_seccion.cod_asig, docente_asignatura_seccion.cod_sec))
        docente_asignatura_seccion.cod_doc_asig_sec = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_doc_asig_sec):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_doc_asig_sec, cod_docente, cod_asig, cod_sec FROM docente_asignatura_seccion WHERE cod_doc_asig_sec = %s", (cod_doc_asig_sec,))
        row = cursor.fetchone()
        if row:
            return DocenteAsignaturaSeccion(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_doc_asig_sec, cod_docente, cod_asig, cod_sec FROM docente_asignatura_seccion")
        rows = cursor.fetchall()
        return [DocenteAsignaturaSeccion(*row) for row in rows]

    def update(self, docente_asignatura_seccion):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE docente_asignatura_seccion SET cod_docente = %s, cod_asig = %s, cod_sec = %s WHERE cod_doc_asig_sec = %s", 
                       (docente_asignatura_seccion.cod_docente, docente_asignatura_seccion.cod_asig, docente_asignatura_seccion.cod_sec, docente_asignatura_seccion.cod_doc_asig_sec))
        self.connection.commit()

    def delete(self, cod_doc_asig_sec):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM docente_asignatura_seccion WHERE cod_doc_asig_sec = %s", (cod_doc_asig_sec,))
        self.connection.commit()

    def get_id_by_rut_identificador_seccion(self, rut, identificador, seccion):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_doc_asig_sec FROM docente_asignatura_seccion das "
                       "JOIN docente d ON das.cod_docente = d.cod_docente "
                       "JOIN asignatura a ON das.cod_asig = a.cod_asig "
                       "JOIN seccion s ON das.cod_sec = s.cod_sec "
                       "WHERE d.rut = %s AND a.identificador = %s AND s.seccion = %s", (rut, identificador, seccion))
        row = cursor.fetchone()
        if row:
            return row[0]
        return None


class BloqueHorarioDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, bloque_horario):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO bloque_horario (hora_inicio, hora_fin) "
                       "VALUES (%s, %s) RETURNING bloque", 
                       (bloque_horario.hora_inicio, bloque_horario.hora_fin))
        bloque_horario.bloque = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, bloque):
        cursor = self.connection.cursor()
        cursor.execute("SELECT bloque, hora_inicio, hora_fin FROM bloque_horario WHERE bloque = %s", (bloque,))
        row = cursor.fetchone()
        if row:
            return BloqueHorario(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT bloque, hora_inicio, hora_fin FROM bloque_horario")
        rows = cursor.fetchall()
        return [BloqueHorario(*row) for row in rows]

    def update(self, bloque_horario):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE bloque_horario SET hora_inicio = %s, hora_fin = %s WHERE bloque = %s", 
                       (bloque_horario.hora_inicio, bloque_horario.hora_fin, bloque_horario.bloque))
        self.connection.commit()

    def delete(self, bloque):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM bloque_horario WHERE bloque = %s", (bloque,))
        self.connection.commit()


class SalaDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, sala):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO sala (cod_edificio, cod_ori, sala, capacidad, volumen, cod_controlador) "
                       "VALUES (%s, %s, %s, %s, %s) RETURNING cod_sala", 
                       (sala.cod_edificio, sala.cod_ori, sala.sala, sala.capacidad, sala.volumen,sala.cod_controlador))
        sala.cod_sala = cursor.fetchone()[0]
        self.connection.commit()
    
    def get_by_id(self, cod_sala):
        cursor = self.connection.cursor()
        cursor.execute("SELECT  FROM sala WHERE cod_sala = %s", (cod_sala,))
        row = cursor.fetchone()
        if row:
            return Sala(*row)
        return None
    
    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_sala, cod_edificio, cod_ori, sala, capacidad, volumen, cod_controlador FROM sala")
        rows = cursor.fetchall()
        return [Sala(*row) for row in rows]
    
    def update(self, sala):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE sala SET cod_edificio = %s, cod_ori = %s, sala = %s, capacidad = %s, volumen = %s, cod_controlador = %s WHERE cod_sala = %s",
                       (sala.cod_edificio, sala.cod_ori, sala.sala, sala.capacidad, sala.volumen, sala.cod_controlador, sala.cod_sala))
        self.connection.commit()

    def delete(self, cod_sala):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM sala WHERE cod_sala = %s", (cod_sala,))
        self.connection.commit()

    def get_id_by_sala(self, sala):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_sala FROM sala WHERE sala = %s", (sala,))
        row = cursor.fetchone()
        if row:
            return row[0]
        return None


class ClaseDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, clase):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO clase (cod_doc_asig_sec, cod_sala, sala_real, fecha) "
                       "VALUES (%s, %s, %s, %s) RETURNING cod_clase",
                       (clase.cod_doc_asig_sec, clase.cod_sala, clase.sala_real, clase.fecha))
        clase.cod_clase = cursor.fetchone()[0]
        self.connection.commit()
    
    def get_by_id(self, cod_clase):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_clase, cod_doc_asig_sec, cod_sala, sala_real, fecha FROM clase WHERE cod_clase = %s", (cod_clase,))
        row = cursor.fetchone()
        if row:
            return Clase(*row)
        return None
    
    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_clase, cod_doc_asig_sec, cod_sala, sala_real, fecha FROM clase")
        rows = cursor.fetchall()
        return [Clase(*row) for row in rows]
    
    def update(self, clase):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE clase SET cod_doc_asig_sec = %s, cod_sala = %s, sala_real = %s, fecha = %s WHERE cod_clase = %s",
                       (clase.cod_doc_asig_sec, clase.cod_sala, clase.sala_real, clase.fecha, clase.cod_clase))
        self.connection.commit()

    def delete(self, cod_clase):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM clase WHERE cod_clase = %s", (cod_clase,))
        self.connection.commit()

    def get_id_by_clase(self, cod_doc_asig_sec, cod_sala, fecha):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_clase FROM clase WHERE cod_doc_asig_sec = %s AND cod_sala = %s AND fecha = %s", (cod_doc_asig_sec, cod_sala, fecha))
        row = cursor.fetchone()
        if row:
            return row[0]
        return None


class SedeDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, sede):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO sede (nombre, cod_comuna) "
                       "VALUES (%s, %s) RETURNING cod_sede",
                       (sede.nombre, sede.cod_comuna))
        sede.cod_sede = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_sede):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_sede, nombre, cod_comuna FROM sede WHERE cod_sede = %s", (cod_sede,))
        row = cursor.fetchone()
        if row:
            return Sede(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_sede, nombre, cod_comuna FROM sede")
        rows = cursor.fetchall()
        return [Sede(*row) for row in rows]

    def update(self, sede):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE sede SET nombre = %s, cod_comuna = %s WHERE cod_sede = %s",
                       (sede.nombre,sede.cod_comuna, sede.cod_sede))
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
        cursor.execute("INSERT INTO edificio (cod_sede, nombre) "
                       "VALUES (%s, %s) RETURNING cod_edificio", 
                       (edificio.cod_sede, edificio.nombre))
        edificio.cod_edificio = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_edificio):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_edificio, cod_sede, nombre FROM edificio WHERE cod_edificio = %s", (cod_edificio,))
        row = cursor.fetchone()
        if row:
            return Edificio(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_edificio, cod_sede, nombre FROM edificio")
        rows = cursor.fetchall()
        return [Edificio(*row) for row in rows]

    def update(self, edificio):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE edificio SET cod_sede = %s, nombre = %s WHERE cod_edificio = %s", 
                       (edificio.cod_sede, edificio.nombre, edificio.cod_edificio))
        self.connection.commit()

    def delete(self, cod_edificio):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM edificio WHERE cod_edificio = %s", (cod_edificio,))
        self.connection.commit()


class BloqueClaseDAO:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, bloque_clase):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO bloque_clase (cod_clase, bloque) "
                       "VALUES (%s, %s) RETURNING cod_bloque_clase",
                       (bloque_clase.cod_clase, bloque_clase.bloque))
        bloque_clase.cod_bloque_clase = cursor.fetchone()[0]
        self.connection.commit()

    def get_by_id(self, cod_bloque_clase):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_bloque_clase, cod_clase, bloque FROM bloque_clase WHERE cod_bloque_clase = %s", (cod_bloque_clase,))
        row = cursor.fetchone()
        if row:
            return BloqueClase(*row)
        return None

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_bloque_clase, cod_clase, bloque FROM bloque_clase")
        rows = cursor.fetchall()
        return [BloqueClase(*row) for row in rows]

    def update(self, bloque_clase):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE bloque_clase SET cod_clase = %s, bloque = %s WHERE cod_bloque_clase = %s",
                       (bloque_clase.cod_clase, bloque_clase.bloque, bloque_clase.cod_bloque_clase))
        self.connection.commit()

    def delete(self, cod_bloque_clase):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM bloque_clase WHERE cod_bloque_clase = %s", (cod_bloque_clase,))
        self.connection.commit()

    def get_id_by_clase_bloque(self, cod_clase, bloque):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cod_bloque_clase FROM bloque_clase WHERE cod_clase = %s AND bloque = %s", (cod_clase, bloque))
        row = cursor.fetchone()
        if row:
            return row[0]
        return None