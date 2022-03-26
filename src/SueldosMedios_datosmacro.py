import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
data = []
r = requests.get('https://datosmacro.expansion.com/mercado-laboral/salario-medio')
soup = BeautifulSoup(r.text, 'lxml')
table=soup.find('table')
table_body=table.find('tbody')
rows=table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values
print(tabulate(data, headers=["País", "Año",  "SalMed Local","Moneda","SalMed $","SalMed €", "Var"]))
