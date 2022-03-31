import pandas as pd
import numpy as np


def clean_csv():

    dataset_sueldos = pd.read_csv('dataset_sueldos.csv', delimiter=',')

    # Hay una oferta de San Francisco que contiene una oferta de la Universidad de Canberra, otra de la india e incluso Brasil
    # No nos interesan. Nos quedamos solo con ofertas en euros o dolares. Vamos a suponer que el valor del dolar y el euro es similar
    dataset_sueldos = dataset_sueldos[dataset_sueldos['Sueldo'].str.contains('€|\$') == True]
    dataset_sueldos = dataset_sueldos.reset_index()


    # Limpiamos el campo de Sueldo
    dataset_sueldos['Sueldo texto limpio'] = dataset_sueldos['Sueldo'].str.lower()
    dataset_sueldos['Sueldo texto limpio'] = dataset_sueldos['Sueldo texto limpio'].str.replace('sobre', '')
    dataset_sueldos['Sueldo texto limpio'] = dataset_sueldos['Sueldo texto limpio'].str.replace('€', '')
    dataset_sueldos['Sueldo texto limpio'] = dataset_sueldos['Sueldo texto limpio'].str.replace('por hora', '')
    dataset_sueldos['Sueldo texto limpio'] = dataset_sueldos['Sueldo texto limpio'].str.replace('/año', '')
    dataset_sueldos['Sueldo texto limpio'] = dataset_sueldos['Sueldo texto limpio'].str.replace('/mes', '')
    dataset_sueldos['Sueldo texto limpio'] = dataset_sueldos['Sueldo texto limpio'].str.replace('.', '')
    dataset_sueldos['Sueldo texto limpio'] = dataset_sueldos['Sueldo texto limpio'].str.replace(' ', '')
    dataset_sueldos['Sueldo texto limpio'] = dataset_sueldos['Sueldo texto limpio'].str.replace(u'\xa0', '')
    dataset_sueldos['Sueldo texto limpio'] = dataset_sueldos['Sueldo texto limpio'].str.replace('/h', '')
    dataset_sueldos['Sueldo texto limpio'] = dataset_sueldos['Sueldo texto limpio'].str.replace('us\$', '')
    dataset_sueldos['Sueldo texto limpio'] = dataset_sueldos['Sueldo texto limpio'].str.replace('ca\$', '')



    dataset_sueldos['Sueldo anual'] = ""

    for row in range(dataset_sueldos.shape[0]):

        if '-' in dataset_sueldos['Sueldo texto limpio'][row]:
            valores = dataset_sueldos['Sueldo texto limpio'][row].split('-')

            for i in range(len(valores)):
                if 'mil' in valores[i]:
                    valores[i] = valores[i].replace('mil', '')
                    valores[i] = 1000 * int(valores[i])
                else:
                    valores[i] = int(valores[i])

            dataset_sueldos['Sueldo texto limpio'][row] = np.mean(valores)

        if 'mes' in dataset_sueldos['Periodo'][row]:
            dataset_sueldos['Sueldo anual'][row] = int(dataset_sueldos['Sueldo texto limpio'][row]) * 12
        elif 'hora' in dataset_sueldos['Periodo'][row]:
            # Numero aproximado de horas trabajadas al año: 1725
            dataset_sueldos['Sueldo anual'][row] = int(dataset_sueldos['Sueldo texto limpio'][row]) * 1725
        else:
            dataset_sueldos['Sueldo anual'][row] = dataset_sueldos['Sueldo texto limpio'][row]

    del dataset_sueldos['Sueldo texto limpio']
    del dataset_sueldos['Periodo']
    del dataset_sueldos['index']

    dataset_sueldos['Sueldo anual'] = dataset_sueldos['Sueldo anual'].astype('int')

    dataset_sueldos.to_csv('dataset_sueldos_clean.csv', index=False)

    #Pasamos a limpiar el CSV de SMI
    SMI_dataset=pd.read_csv('SMI.csv', delimiter=',',encoding='utf-8')

    SMI_dataset['País'] = SMI_dataset['País'].str.replace(']', '')
    SMI_dataset['País'] = SMI_dataset['País'].str.replace('+', '')
    SMI_dataset['País'] = SMI_dataset['País'].str.replace('[', '')
    SMI_dataset['País'] = SMI_dataset['País'].str.strip()
    SMI_dataset['SalMed €']=SMI_dataset['SalMed €'].str.replace('€', '')
    SMI_dataset['SalMed €'] = SMI_dataset['SalMed €'].str.replace('.', '')
    SMI_dataset['SalMed €'] = SMI_dataset['SalMed €'].str.replace(u'\xa0', '')
    #Pasamos la columna a Integer
    SMI_dataset['SalMed €'] = SMI_dataset['SalMed €'].fillna(-1)
    SMI_dataset['SalMed €'] = SMI_dataset['SalMed €'].astype('int')

    return dataset_sueldos , SMI_dataset




