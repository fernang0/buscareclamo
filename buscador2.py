import requests
from bs4 import BeautifulSoup
url = "https://www.reclamos.cl/empresa/correos_de_chile";
palabra_clave = ["conserje", "se-entrego-mal", "devuelto", "aparece-entregado", "entregado", "no-hay-quien-reciba"];
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'};
datos = open("datos.txt", "a");

for numpage in range(1, 443, 1):
    urlpage = url+"?page="+str(numpage);
    response = requests.get(urlpage, headers=headers);

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser');
        for link in soup.find_all('a'):
            for palabra in palabra_clave:
                if palabra in link.get('href'):
                    datos.write(f"{link.get('href')}\n");
                    print(f"coincidencia encontrada de: {palabra}, en: {link.get('href')}");
    else:
        print(f"Error al obtener el contenido de la pagina {urlpage}, codigo de error: {response.status_code}");
