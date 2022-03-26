import pandas as pd
import numpy as np


def clean_csv():

    dataset_sueldos = pd.read_csv('dataset_sueldos.csv', delimiter=',')

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

    # Hay una oferta de San Francisco que contiene una oferta de la Universidad de Canberra, otra de la india e incluso Brasil
    # No nos interesan.
    dataset_sueldos = dataset_sueldos[dataset_sueldos['Sueldo texto limpio'].str.contains('aud|inr|brl') == False]
    dataset_sueldos = dataset_sueldos.reset_index()

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

    dataset_sueldos.to_csv('dataset_sueldos_clean.csv', index=False)

    return dataset_sueldos




