import requests
from bs4 import BeautifulSoup
import pandas as pd


#Descarga completa de una ciudad

def sueldos(ciudad, dataset_sueldos):

    #Añadimos un header para que no nos detecten como bots
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\
    */*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch, br",
        "Accept-Language": "en-US,en;q=0.8",
        "Cache-Control": "no-cache",
        "dnt": "1",
        "Pragma": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/5\
    37.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    }

    #Cada ciudad tiene un codigo diferente en la web, que hemos ido recopilando en un CSV
    lista_codigos = pd.read_csv('codigos.csv', delimiter=',')

    url_base = "https://www.glassdoor.es/Sueldos/"
    url_puesto = "-data-scientist-sueldo-"

    #Pasamos ciudad a lower por si se ha escrito de otra manera
    ciudad = ciudad.lower()

    if lista_codigos[lista_codigos["ciudad"] == ciudad]['codigo'].empty:
        print('No tenemos esta ciudad entre las almacenadas en los codigos.')
        return 0
    else:
        codigo_ciudad = lista_codigos[lista_codigos["ciudad"] == ciudad]['codigo'].item()

        #Ciudades con nombres computestos: cambiamos el espacio por un guion
        ciudad_url=ciudad.replace(' ','-')

    url_completa = url_base + ciudad_url + url_puesto + codigo_ciudad + ".htm"

    page = requests.get(url_completa, headers=headers)

    if page.status_code == 200:
        soup = BeautifulSoup(page.content, "html.parser")
    else:
        print("HTTP error: ", page.status_code)
        return 0

    texto_paginas = soup.find('div', {'class': 'paginationFooter'}).text

    texto_paginas_sp = texto_paginas.split()

    total_paginas = int(texto_paginas_sp[-1])

    for pagina in range(total_paginas):

        print("Ciudad: ",ciudad,". Pagina ",pagina+1," de un total de ",total_paginas)

        url_completa = url_base + ciudad + url_puesto + codigo_ciudad + "_IP" + str(pagina+1) + ".htm"

        page = requests.get(url_completa, headers=headers)

        if page.status_code == 200:
            soup = BeautifulSoup(page.content, "html.parser")
        else:
            print("HTTP error: ", page.status_code)
            return 0

        #Cogemos la parte que nos interesa
        resultados = soup.findAll('div', {'class': 'py css-17435dd'})

        if not resultados:
            #Revisando la web vemos que ha paginas a las que se puede acceder pero ya no tiene la información que buscamos, por lo que paramos cuando ya no encontremos esta etiqueta
            print('Hemos llegado a la ultima pagina con resultados. Pagina: ',pagina+1)

            return dataset_sueldos

        for item in resultados:
            dataset_sueldos = dataset_sueldos.append(
                {'Ciudad': ciudad, 'Empresa': item.find('a', {'class': 'css-f3vw95 e1aj7ssy3'}).text,
                 'Sueldo': item.find('div', {'class': 'd-flex align-items-baseline'}).text,
                 'Periodo':item.find('span',{'class':'m-0 css-18stkbk'}).text}, ignore_index=True)

    return dataset_sueldos

