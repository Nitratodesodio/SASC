class Modalidad:
    def __init__(self, cod_mod, modalidad):
        self.cod_mod = cod_mod
        self.modalidad = modalidad


class Semestre:
    def __init__(self, cod_sem, semestre):
        self.cod_sem = cod_sem
        self.semestre = semestre


class Seccion:
    def __init__(self, cod_sec, seccion):
        self.cod_sec = cod_sec
        self.seccion = seccion


class Docente:
    def __init__(self, cod_docente, rut, nombre, primer_apellido, segundo_apellido):
        self.cod_docente = cod_docente
        self.rut = rut
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido

class Asignatura:
    def __init__(self, cod_asig, cod_mod, cod_sem, identificador, nombre):
        self.cod_asig = cod_asig
        self.nombre = nombre
        self.cod_mod = cod_mod
        self.cod_sem = cod_sem
        self.identificador = identificador


class DocenteAsignaturaSeccion:
    def __init__(self, cod_doc_asig_sec, cod_docente, cod_asig, cod_sec):
        self.cod_docente = cod_docente
        self.cod_asig = cod_asig
        self.cod_sec = cod_sec
        self.cod_doc_asig_sec = cod_doc_asig_sec

class Clase:
    def __init__(self, cod_clase, cod_doc_asig_sec, cod_sala, bloque, sala_real, fecha):
        self.cod_clase = cod_clase
        self.cod_doc_asig_sec = cod_doc_asig_sec
        self.cod_sala = cod_sala
        self.bloque = bloque
        self.sala_real = sala_real
        self.fecha = fecha


class BloqueHorario:
    def __init__(self, bloque, hora_inicio, hora_fin):
        self.bloque = bloque
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin


class Sala:
    def __init__(self, cod_sala, cod_edificio, cod_ori, numero, capacidad, volumen):
        self.cod_sala = cod_sala
        self.cod_edificio = cod_edificio
        self.cod_ori = cod_ori
        self.numero = numero
        self.capacidad = capacidad
        self.volumen = volumen


class Sede:
    def __init__(self, cod_sede, cod_comuna, nombre):
        self.cod_sede = cod_sede
        self.nombre = nombre
        self.cod_comuna = cod_comuna

class Edificio:
    def __init__(self, cod_edificio, cod_sede, nombre):
        self.cod_edificio = cod_edificio
        self.cod_sede = cod_sede
        self.nombre = nombre