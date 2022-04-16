# Título Ejercicio: Practica Cargado y Filtrado (Pandas)
# Autor: Jaime Sepúlveda
# [Bootcamp Data Science  Coding Dojo]

import pandas as pd

# Cargando los datos e instanciando en el objeto DF bike_df
filename = "./data/RailsToTrails_National_Count_Data_week.xlsx"
bike_df = pd.read_excel(filename)

# Eliminando columnas
elimina_columns = bike_df.drop(columns=['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9'])

# Renombrando columnas
renombra_columns = bike_df.rename(columns={'Unnamed: 6': 'percent_change'})

print(elimina_columns)
print(renombra_columns)
print(bike_df.info())

# 52 datos faltantes
# Columnas: 2021 Counts, Unnamed 7, Unnamed 8 y Unnamed 9

print(bike_df.loc[:, '2021 Counts'].fillna(0))
