#!/usr/bin/env python3

import os


directorio_actual= os.getcwd() # Comando pwd
print(f"\n[+] Directorio actual de trabajo: {directorio_actual}")


files= os.listdir(directorio_actual) # Comando ls | Se almacena en una lista
print(f"\n[+] Mostrando archivos en el directorio actual de trabajo: \n")
for i in files: # Para ver el contenido de la lista creamos un bucle for
  print(i)


if not os.path.exists('mi_directorio'): # Si no existe en el directorio actual
  os.mkdir('mi_directorio') # Comando mkdir
  print(f"\n[+] Directorio 'mi_directorio' creado: ")


get_env= os.getenv('SHELL') # Muestra la ruta de la variable de entorno
print(f"\n[+] Valor de la variable de entorno 'SHELL': {get_env}")

