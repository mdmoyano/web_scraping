import pandas as pd
import numpy as np

#Ignorar los FutureWarnings de Pandas/append
import warnings
warnings.simplefilter(action='ignore', category=Warning)

sueldos_dataset = pd.read_csv('dataset_sueldos.csv',delimiter=',')


#Limpiamos el campo de Sueldo
sueldos_dataset['Sueldo texto limpio']= sueldos_dataset['Sueldo'].str.lower()
sueldos_dataset['Sueldo texto limpio']= sueldos_dataset['Sueldo texto limpio'].str.replace('sobre','')
sueldos_dataset['Sueldo texto limpio']= sueldos_dataset['Sueldo texto limpio'].str.replace('€','')
sueldos_dataset['Sueldo texto limpio']= sueldos_dataset['Sueldo texto limpio'].str.replace('por hora','')
sueldos_dataset['Sueldo texto limpio']= sueldos_dataset['Sueldo texto limpio'].str.replace('/año','')
sueldos_dataset['Sueldo texto limpio']= sueldos_dataset['Sueldo texto limpio'].str.replace('/mes','')
sueldos_dataset['Sueldo texto limpio']= sueldos_dataset['Sueldo texto limpio'].str.replace('.','')
sueldos_dataset['Sueldo texto limpio']= sueldos_dataset['Sueldo texto limpio'].str.replace(' ','')
sueldos_dataset['Sueldo texto limpio']= sueldos_dataset['Sueldo texto limpio'].str.replace(u'\xa0','')

sueldos_dataset['Sueldo anual']=""

for row in range(sueldos_dataset.shape[0]):

    if '-' in sueldos_dataset['Sueldo texto limpio'][row]:
        valores=sueldos_dataset['Sueldo texto limpio'][row].split('-')



        for i in range(len(valores)):
            if 'mil' in valores[i]:
                valores[i]=valores[i].replace('mil','')
                valores[i]=1000*int(valores[i])
            else:
                valores[i]=int(valores[i])

        sueldos_dataset['Sueldo anual'][row]=np.mean(valores)

    if 'mes' in sueldos_dataset['Periodo'][row]:
        sueldos_dataset['Sueldo anual'][row] = sueldos_dataset['Sueldo anual'][row]*12
    elif 'hora' in sueldos_dataset['Periodo'][row]:
        #Numero aproximado de horas trabajadas al año: 1725
        sueldos_dataset['Sueldo anual'][row] = sueldos_dataset['Sueldo anual'][row]*1725

print(sueldos_dataset)






