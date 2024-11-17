import psycopg2 as pg
import pandas as pd
from pathlib import PurePath
from dto import *
from dao import *

conn = pg.connect(
    host='localhost',
    database='SCC_v4',
    user='postgres',
    password='root',
    port='5432'
)


def get_data(archivo, hoja, headers, skiprows, usecols):
    with pd.ExcelFile(archivo, engine='openpyxl') as xls:
        df = pd.read_excel(xls,sheet_name=hoja, header=headers, skiprows=skiprows, usecols=usecols)
        return df
"""Ruta del archivo"""
archivo = PurePath("./"+"PLANIFICACION POR DIA- SALA - BLOQUE SEMANA 23-09-2024.xlsx")

"""Parámetros hoja principal"""
planificación = "gestor_1000007014_15148471_1_10"
headers_pln = 0
skiprows_pln = 5
usecols_pln = None

"""Parámetros hoja BLOQUES"""
bloques = "BLOQUES"
headers_bloques = 0
skiprows_bloques = 4
usecols_bloques = "C, D"

"""Dataframes"""
df_bloques = get_data(archivo, bloques, headers_bloques, skiprows_bloques, usecols_bloques)
df_planificación = get_data(archivo, planificación, headers_pln, skiprows_pln, usecols_pln)

"""Bloques almacenados en la BD"""
db_bloques = BloqueHorarioDAO(conn).get_all()
cods_bloques = []
for db_bloque in db_bloques:
    cods_bloques.append(db_bloque.bloque)
#print(db_bloques)

"""Almacenado de bloques"""
for index, row in df_bloques.iterrows():
    if row["BLOQUE"] not in cods_bloques:
        hora_inicio, hora_fin = row["HORARIO"].split(" - ")
        bloque = BloqueHorario(row["BLOQUE"], hora_inicio, hora_fin)
        BloqueHorarioDAO(conn).insert(bloque)
    else:
        print(f"Bloque {row["BLOQUE"]} ya almacenado")

"""Modalidades almacenadas en la BD"""


"""Almacenado de modalidades"""
for index, row in df_planificación.iterrows():
    db_modalidades = ModalidadDAO(conn).get_all()
    modalidades = []
    for db_modalidad in db_modalidades:
        modalidades.append(db_modalidad.modalidad)
    if row["Modalidad"] not in modalidades:
        modalidad = Modalidad(None, row["Modalidad"])
        ModalidadDAO(conn).insert(modalidad)
    else:
        print(f"Modalidad {row["Modalidad"]} ya almacenada")

"""Almacenado de semestres"""
for index, row in df_planificación.iterrows():
    db_semestres = SemestreDAO(conn).get_all()
    semestres = []
    for db_semestre in db_semestres:
        semestres.append(db_semestre.semestre)
    if row["Semestre"] not in semestres:
        semestre = Semestre(None, row["Semestre"])
        SemestreDAO(conn).insert(semestre)
    else:
        print(f"Semestre {row["Semestre"]} ya almacenado")

no_agregados = []
"""Almacenado de secciones"""
for index, row in df_planificación.iterrows():
    db_secciones = SeccionDAO(conn).get_all()
    secciones = []
    for db_seccion in db_secciones:
        secciones.append(db_seccion.seccion)
    if row["Sección"] not in secciones:
        seccion = Seccion(None, row["Sección"])
        if len(row["Sección"]) <= 20:
            SeccionDAO(conn).insert(seccion)
        else:
            if row["Sección"] not in no_agregados:
                no_agregados.append(row["Sección"])
            print(f"Sección {row["Sección"]} no almacenada, excede el límite de caracteres")
    else:
        print(f"Sección {row["Sección"]} ya almacenada")

print(len(df_planificación["Sección"].unique()))
print(len(no_agregados))
#print(df_bloques)

"""Almacenado de docentes"""
for index, row in df_planificación.iterrows():
    db_docentes = DocenteDAO(conn).get_all()
    docentes = []
    for db_docente in db_docentes:
        docentes.append(db_docente.rut)
    if row["Rut Docente"] not in docentes:
        try:
            descomposicion = row["Nombre Docente"].split(" ")
            nombre = descomposicion[:-2]
            primer_apellido = descomposicion[-2]
            segundo_apellido = descomposicion[-1]
            docente = Docente(None, row["Rut Docente"], nombre, primer_apellido, segundo_apellido)
            DocenteDAO(conn).insert(docente)
        except:
            continue
    else:
        print(f"Docente {row["Rut Docente"]} ya almacenado")

