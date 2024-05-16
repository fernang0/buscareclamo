import requests
from bs4 import BeautifulSoup
url = "https://www.reclamos.cl/empresa/correos_de_chile"
palabras_clave = ["se entrego mal", "no realizan entrega", "no entrega", "otra persona", "no hay quien reciba"]
coincidencias = 0;
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

for numpage in range(1,443,1):
    urlpage = url+"?page="+str(numpage)
    response = requests.get(urlpage, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        etiquetas_texto = soup.find_all(text=True)
        for etiqueta in etiquetas_texto:
            texto = etiqueta.lower()
            for palabra in palabras_clave:
                if palabra.lower() in texto:
                    coincidencias += 1
                    print(f"Se encontró una coincidencia de '{palabra}' en: {etiqueta}, {urlpage}")
        
        print(f"Total de coincidencias encontradas: {coincidencias}")
    else:
        print("Error al obtener el contenido de la página", urlpage, response.status_code)