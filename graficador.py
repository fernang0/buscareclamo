import numpy as np
import matplotlib.pyplot as plt
#variables
#ponle las palabras claves que quieras y te dara el grafico
palabra_clave = ["conserje", "devuelto", "otra-persona", "no-entregado", "sucursal"];
frecuencia = np.zeros(len(palabra_clave))
links = open("titulos.txt", "r");
#lo chido
for num in range(1, 1783, 1):
    datos_linea = links.readline(num);
    for id, palabra in enumerate(palabra_clave):
        if palabra in datos_linea:
            frecuencia[id] +=1;
#se crea el grafico con los datos
plt.figure(figsize=(10, 5))
plt.barh(palabra_clave, frecuencia, color='salmon')
plt.xlabel("Frecuencia")
plt.ylabel("Palabras clave")
plt.show()