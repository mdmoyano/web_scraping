import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import csv

#Descargamos el Salario Medio Interprofesional de los diferentes paises

def SMI_FILE():

    data = []
    r = requests.get('https://datosmacro.expansion.com/mercado-laboral/salario-medio')
    soup = BeautifulSoup(r.text, 'lxml')
    table=soup.find('table')
    table_body=table.find('tbody')
    rows=table_body.find_all('tr')

    #Extraemos los datos de la tabla que hay en datosmacro
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    #Los tabulamos para guardarlo posteriormente en un CSV
    SMI=tabulate(data, headers=["País", "Año",  "SalMed Local","Moneda","SalMed $","SalMed €", "Var"],tablefmt="csv")

    with open('SMI.csv','w',encoding = 'utf-8',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["País", "Año",  "SalMed Local","Moneda","SalMed $","SalMed €", "Var"])
        writer.writerows(data)


