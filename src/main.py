import pandas as pd
from descarga import sueldos
from clean import clean_csv
from SMI import SMI_FILE

#Ignorar los FutureWarnings de Pandas/append
import warnings
warnings.simplefilter(action='ignore', category=Warning)


#Empty data frame
dataset_sueldos = pd.DataFrame(columns=['Ciudad', 'Empresa', 'Sueldo','Periodo'])

#Descargamos los datos de las ciudades que nos interesan
dataset_sueldos = sueldos('madrid',dataset_sueldos)
dataset_sueldos = sueldos('San Francisco',dataset_sueldos)
dataset_sueldos = sueldos('barcelona',dataset_sueldos)
dataset_sueldos = sueldos('berlin',dataset_sueldos)
dataset_sueldos = sueldos('paris',dataset_sueldos)
dataset_sueldos = sueldos('bruselas',dataset_sueldos)
dataset_sueldos = sueldos('amsterdam',dataset_sueldos)
dataset_sueldos = sueldos('sevilla',dataset_sueldos)

#Guardamos los datos en un CSV
dataset_sueldos.to_csv('dataset_sueldos.csv',index=False)

#Descargamos los datos del SMI
SMI_FILE()

#Limpiamos dichos CSV
dataset_sueldos_clean,SMI_clean=clean_csv()

del dataset_sueldos_clean['Sueldo']
del dataset_sueldos_clean['Empresa']

#Sacamos la media del salario agrupando por ciudad
media_ciudad=dataset_sueldos_clean.groupby('Ciudad', as_index=False)['Sueldo anual'].mean()

#Finalmente calculamos el sueldo vs Sueldo medio. Añadimos una columna con todo 0
media_ciudad['Sueldo vs Sueldo Medio'] = 0

#Calculamos el ratio
media_ciudad.loc[media_ciudad['Ciudad'].str.contains('sevilla|barcelona|madrid') == True,'Sueldo vs Sueldo Medio'] = media_ciudad.loc[media_ciudad['Ciudad'].str.contains('sevilla|barcelona|madrid') == True,'Sueldo anual']/SMI_clean[SMI_clean['País']=='España']['SalMed €'].iloc[0]
media_ciudad.loc[media_ciudad['Ciudad'] == 'berlin','Sueldo vs Sueldo Medio'] = media_ciudad.loc[media_ciudad['Ciudad'] == 'berlin','Sueldo anual']/SMI_clean[SMI_clean['País']=='Alemania']['SalMed €'].iloc[0]
media_ciudad.loc[media_ciudad['Ciudad'] == 'paris','Sueldo vs Sueldo Medio'] = media_ciudad.loc[media_ciudad['Ciudad'] == 'paris','Sueldo anual']/SMI_clean[SMI_clean['País']=='Francia']['SalMed €'].iloc[0]
media_ciudad.loc[media_ciudad['Ciudad'] == 'amsterdam','Sueldo vs Sueldo Medio'] = media_ciudad.loc[media_ciudad['Ciudad'] == 'amsterdam','Sueldo anual']/SMI_clean[SMI_clean['País']=='Países Bajos']['SalMed €'].iloc[0]
media_ciudad.loc[media_ciudad['Ciudad'] == 'bruselas','Sueldo vs Sueldo Medio'] = media_ciudad.loc[media_ciudad['Ciudad'] == 'bruselas','Sueldo anual']/SMI_clean[SMI_clean['País']=='Bélgica']['SalMed €'].iloc[0]
media_ciudad.loc[media_ciudad['Ciudad'] == 'san francisco','Sueldo vs Sueldo Medio'] = media_ciudad.loc[media_ciudad['Ciudad'] == 'san francisco','Sueldo anual']/SMI_clean[SMI_clean['País']=='Estados Unidos']['SalMed €'].iloc[0]


media_ciudad.to_csv('Sueldos_DataScientist_vs_SMI.csv', index=False)
