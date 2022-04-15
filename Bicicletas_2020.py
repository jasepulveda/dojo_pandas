# Título Ejercicio: Practica Cargado y Filtrado (Pandas)
# Autor Jaime Sepúlveda
# [Bootcamp Data Science  Coding Dojo]

import pandas as pd

# Cargando los datos e instanciando en el objeto DF bike_df
filename = "./data/RailsToTrails_National_Count_Data_week.xlsx"
bike_df = pd.read_excel(filename)

# Aplicando los filtros sobre el DF
filtro_weekof = bike_df['Week of'] >= '2020-07-31'
filtro_change = (bike_df['Change 2019-2020'] * 100) > 100

#Imprimiendo los resultados de los dos primeros filtros
print(bike_df.loc[filtro_weekof, :])
print(bike_df.loc[filtro_change, :])

# Actualizando el DF con el primer filtro
bike_df = bike_df.loc[filtro_weekof, :]

# Filtrado combinado, para evidenciar registros con mayor a un 100%
# posterior al 31 de julio 2020
filtro_semana = bike_df.loc[filtro_weekof & filtro_change, :]

# Imprimiendo resultado filtro combinado
# Nota: No se evidencian registros con valores mayores al 100%
print(filtro_semana)

