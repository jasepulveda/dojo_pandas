# Título Ejercicio: Datos Titanic - Ejercicio Pandas
# Autor: Jaime Sepúlveda
# [Bootcamp Data Science  Coding Dojo]

import pandas as pd

# Cargando los datos e instanciando en el objeto
filename = "./data/titanic.csv"
df = pd.read_csv(filename)

# Monstrando la cabecera de la trama de datos
print(df)

# Calculando el % de sobrevivientes
media_survived = (df['Survived'].mean()) * 100
fare = df['Fare'] < 10

# Filtrando sobrevivientes hombres y mujeres
survived = df['Survived'] == 1
no_survived = df['Survived'] == 0
male = df['Sex'] == 'male'
female = df['Sex'] == 'female'
male_survived = df.loc[survived & male].count()
female_survived = df.loc[survived & female].count()

fare_survived = df.loc[survived & fare].count()

age_prom = df['Age']
age_prom_nosurv = df.loc[no_survived & age_prom, :].mean()
age_prom_surv = df.loc[survived & age_prom, :].mean()

age_prom_sex_surv_male = df.loc[survived & male].mean()
age_prom_sex_surv_female = df.loc[no_survived & female].mean()


print(f'Porcentaje de personas sobrevivientes %: {media_survived:,.2f}')
print('Hombres: ', male_survived.head(1))
print('Mujeres: ', female_survived.head(1))
print('% de pasajes menor a US$ 10', (fare_survived.head(1) * 100) / df.count().head(1))
print(age_prom_nosurv)      # Promedio de edad no sobrevivientes 30 años
print(age_prom_surv)        # Promedio de edad de sobrevivientes 28 años

print(age_prom_sex_surv_male)       # Promedio de edad hombres sobrevivientes 27 años
print(age_prom_sex_surv_female)     # Promedio de edad mujeres sobrevivientes 25 años




