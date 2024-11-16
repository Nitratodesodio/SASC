import psycopg2 as pg
import pandas as pd
import openpyxl
from pathlib import PurePath
from dto import *
from dao import *

conn = pg.connect(
    host='localhost',
    database='RPA',
    user='root',
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

"""Almacenado de bloques"""
for index, row in df_bloques.iterrows():
    #print(row["BLOQUE"], row["HORA INICIO"])
    if row["BLOQUE"] not in db_bloques:
        BloqueHorarioDAO.insert()


#print(get_data(archivo, hoja, headers, skiprows, usecols))

