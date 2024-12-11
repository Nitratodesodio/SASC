import psycopg2 as pg
import pandas as pd
from pathlib import PurePath
from .dao import *


def get_data(archivo, hoja, headers, skiprows, usecols):
    with pd.ExcelFile(archivo, engine='openpyxl') as xls:
        df = pd.read_excel(xls,sheet_name=hoja, header=headers, skiprows=skiprows, usecols=usecols)
        return df

def cargar_clases(archivo):
    conn = pg.connect(
        host='34.201.62.144',
        database='scc',
        user='postgres',
        password='postgres',
        port='5432'
    )
    #Parámetros hoja principal
    planificacion = 0
    headers_pln = 0
    skiprows_pln = 5
    usecols_pln = "G, I, L, T, Y, Z"

    #Almacenado de clases
    clases = get_data(archivo, planificacion, headers_pln, skiprows_pln, usecols_pln)
    clases_unicas = { (identificador, rut, seccion, sala, fecha, bloque) for identificador, rut, seccion, sala, fecha, bloque in clases.itertuples(index=False,name=None)}

    for identificador, rut, seccion, sala, fecha, bloque in clases_unicas:
        if rut != "-":
            cod_doc_asig_sec = DocenteAsignaturaSeccionDAO(conn).get_id_by_rut_identificador_seccion(str(rut), str(identificador), str(seccion))
            cod_sala = SalaDAO(conn).get_id_by_sala(str(sala))
            if not ClaseDAO(conn).get_id_by_clase(cod_doc_asig_sec, cod_sala, fecha):
                ClaseDAO(conn).insert(Clase(None, cod_doc_asig_sec, cod_sala, None, fecha))
            else:
                print(f"Clase {identificador} {rut} {seccion} {sala} {fecha} ya almacenada")
            cod_clase = ClaseDAO(conn).get_id_by_clase(cod_doc_asig_sec, cod_sala, fecha)
            cod_bloque_clase = BloqueClaseDAO(conn).get_id_by_clase_bloque(cod_clase, bloque)
            if not cod_bloque_clase:
                BloqueClaseDAO(conn).insert(BloqueClase(None, cod_clase, bloque))
            else:
                print(f"Bloque {cod_bloque_clase} ya almacenado")

    conn.close()