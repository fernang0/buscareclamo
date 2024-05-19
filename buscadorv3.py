import requests
import pandas as pd
from bs4 import BeautifulSoup

dataframe = []
url = "https://www.reclamos.cl/empresa/correos_de_chile"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

for numpage in range(1,100, 1):
    link = url+"?page="+str(numpage);
    response = requests.get(link, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        for tr in soup.find_all(class_="normal odd"):
            datos = []
            
            td_fecha = tr.find(class_="view-field view-field-node_created")
            if td_fecha:
                fecha = td_fecha.text.strip()
                datos.append(fecha)
            else:
                datos.append("None")
            td_title = tr.find(class_="view-field view-field-node_title")
            if td_title:
                estado = td_title.find(class_="badge")
                if estado:
                    datos.append(estado.text.strip().lower())
                else:
                    datos.append("None")
                
                titulo = td_title.find("a")
                if titulo:
                    datos.append(titulo.text.strip().lower())
                else:
                    datos.append("None")
            else:
                datos.extend(["None", "None"])
        for tr in soup.find_all(class_="normal even"):
            datos = []
            
            td_fecha = tr.find(class_="view-field view-field-node_created")
            if td_fecha:
                fecha = td_fecha.text.strip()
                datos.append(fecha)
            else:
                datos.append("None")
            td_title = tr.find(class_="view-field view-field-node_title")
            if td_title:
                estado = td_title.find(class_="badge")
                if estado:
                    datos.append(estado.text.strip().lower())
                else:
                    datos.append("None")
                
                titulo = td_title.find("a")
                if titulo:
                    datos.append(titulo.text.strip().lower())
                else:
                    datos.append("None")
            else:
                datos.extend(["None", "None"])

            dataframe.append({"Fecha": datos[0], "Estado": datos[1], "Enunciado": datos[2]})
    else:
        print(f"Error en: {url}, codigo: {response.status_code}")

df = pd.DataFrame(dataframe)

df.to_excel('out.xlsx')
df.to_csv('out.csv')