# Título Ejercicio: Estatura Promedio
# Autor: Jaime Sepúlveda
# [Bootcamp Data Science  Coding Dojo]

import pandas as pd

filename = "./data/athlete_events.csv"

df = pd.read_csv(filename)
df_estatura = df.groupby(['ID', 'Year'])['Height'].mean()

print(df_estatura)