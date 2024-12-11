import psycopg2 as pg
import pandas as pd
from pathlib import PurePath
from carga_planificacion.dto import *
from carga_planificacion.dao import *



def get_data(archivo, hoja, headers, skiprows, usecols):
    with pd.ExcelFile(archivo, engine='openpyxl') as xls:
        df = pd.read_excel(xls,sheet_name=hoja, header=headers, skiprows=skiprows, usecols=usecols)
        return df

def cargar_datos(archivo):
    conn = pg.connect(
        host='34.201.62.144',
        database='postgres',
        user='postgres',
        password='postgres',
        port='5432'
    )
    """Parámetros hoja principal"""
    planificacion = 0
    headers_pln = 0
    skiprows_pln = 5
    usecols_pln = None

    """Parámetros hoja BLOQUES"""
    bloques = "BLOQUES"
    headers_bloques = 0
    skiprows_bloques = 4
    usecols_bloques = "C, D"

    """Dataframes"""

    df_planificacion = get_data(archivo, planificacion, headers_pln, skiprows_pln, usecols_pln)

    try:
        df_bloques = get_data(archivo, bloques, headers_bloques, skiprows_bloques, usecols_bloques)
        """Almacenado de Bloques"""
        for index, bloque in df_bloques.iterrows():
            if not BloqueHorarioDAO(conn).get_by_id(bloque["BLOQUE"]):
                hora_inicio, hora_fin = bloque["HORARIO"].split(" - ")
                BloqueHorarioDAO(conn).insert(BloqueHorario(bloque["BLOQUE"], hora_inicio, hora_fin))
            else:
                print(f"Bloque {bloque['BLOQUE']} ya almacenado")
    except:
        print("No se encontró la hoja BLOQUES")

    """Filtro de filas únicas"""
    modalidades = df_planificacion["Modalidad"].unique()
    semestres = df_planificacion["Semestre"].unique()
    secciones = df_planificacion["Sección"].unique()
    salas = df_planificacion["Sala Planificada"].unique()

    for modalidad in modalidades:
        if not ModalidadDAO(conn).get_id_by_modalidad(modalidad):
            ModalidadDAO(conn).insert(Modalidad(None, modalidad))
        else:
            print(f"Modalidad {modalidad} ya almacenada")

    for semestre in semestres:
        if not SemestreDAO(conn).get_id_by_semestre(str(semestre)):
            SemestreDAO(conn).insert(Semestre(None, str(semestre)))
        else:
            print(f"Semestre {semestre} ya almacenado")

    for seccion in secciones:
        if not SeccionDAO(conn).get_id_by_seccion(seccion):
            SeccionDAO(conn).insert(Seccion(None, seccion))
        else:
            print(f"Sección {seccion} ya almacenada")

    for sala in salas:
        if not SalaDAO(conn).get_id_by_sala(str(sala)):
            SalaDAO(conn).insert(Sala(None, None, None, str(sala), None, None, None))
        else:
            print(f"Sala {sala} ya almacenada")

    """Almacenado de docentes, asignaturas y docentes asignaturas secciones"""
    docentes = get_data(archivo, planificacion, headers_pln, skiprows_pln, "I, J")
    docentes_unicos = { (rut,docente) for rut, docente in docentes.itertuples(index=False,name=None)}

    for rut, docente in docentes_unicos:
        if not DocenteDAO(conn).get_id_by_rut(rut) and rut != "-":
            docente = str(docente).split(" ")
            nombre = docente[:-2]
            primer_apellido = docente[-2]
            segundo_apellido = docente[-1]
            DocenteDAO(conn).insert(Docente(None, rut, nombre, primer_apellido, segundo_apellido))
        else:
            print(f"Docente {rut} ya almacenado")

    asignaturas = get_data(archivo, planificacion, headers_pln, skiprows_pln, "P, F, G, H")
    asignaturas_unicas = { (semestre, identificador, nombre, modalidad) for semestre, identificador, nombre, modalidad in asignaturas.itertuples(index=False,name=None)}

    for semestre, identificador, nombre, modalidad in asignaturas_unicas:
        if not AsignaturaDAO(conn).get_id_by_identificador(identificador):
            cod_mod = ModalidadDAO(conn).get_id_by_modalidad(modalidad)
            cod_sem = SemestreDAO(conn).get_id_by_semestre(str(semestre))
            AsignaturaDAO(conn).insert(Asignatura(None, cod_mod, cod_sem, identificador, nombre))
        else:
            print(f"Asignatura {identificador} ya almacenada")

    docentes_asignaturas_secciones = get_data(archivo, planificacion, headers_pln, skiprows_pln, "G, I, L")
    docentes_asignaturas_secciones_unicas = { (identificador, rut, seccion) for identificador, rut, seccion in docentes_asignaturas_secciones.itertuples(index=False,name=None)}

    for identificador, rut, seccion in docentes_asignaturas_secciones_unicas:
        if not DocenteAsignaturaSeccionDAO(conn).get_id_by_rut_identificador_seccion(rut, identificador, seccion) and rut != "-":
            cod_docente = DocenteDAO(conn).get_id_by_rut(rut)
            cod_asig = AsignaturaDAO(conn).get_id_by_identificador(identificador)
            cod_sec = SeccionDAO(conn).get_id_by_seccion(seccion)
            DocenteAsignaturaSeccionDAO(conn).insert(DocenteAsignaturaSeccion(None, cod_docente, cod_asig, cod_sec))
        else:
            print(f"Docente {rut} asignatura {identificador} sección {seccion} ya almacenado")


    conn.close()