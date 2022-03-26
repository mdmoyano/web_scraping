import pandas as pd
from descarga import sueldos
from clean import clean_csv

#Ignorar los FutureWarnings de Pandas/append
import warnings
warnings.simplefilter(action='ignore', category=Warning)


#Empty data frame
dataset_sueldos = pd.DataFrame(columns=['Ciudad', 'Empresa', 'Sueldo','Periodo'])

dataset_sueldos = sueldos('madrid',dataset_sueldos)
dataset_sueldos = sueldos('San Francisco',dataset_sueldos)
dataset_sueldos = sueldos('barcelona',dataset_sueldos)
dataset_sueldos = sueldos('berlin',dataset_sueldos)
dataset_sueldos = sueldos('paris',dataset_sueldos)
dataset_sueldos = sueldos('bruselas',dataset_sueldos)
dataset_sueldos = sueldos('amsterdam',dataset_sueldos)
dataset_sueldos = sueldos('sevilla',dataset_sueldos)

dataset_sueldos.to_csv('dataset_sueldos.csv',index=False)

dataset_sueldos_clean=clean_csv()



