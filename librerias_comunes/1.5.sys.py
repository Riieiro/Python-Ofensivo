#!/usr/bin/env

import sys

print(f"\n[+] Nombre del script: {sys.argv[0]}") # Mostramos el nombre del archivo
print(f"[+] Total de argumentos que se están pasando al programa: {len(sys.argv)}") # Monstramos la cantidad de parámetros
print(f"[+] Mostrando todos los argumentos: {sys.argv}") # Mostramos todos los parámetros


print(f"\n[+] Mostrando las rutas de Python: \n")
for i in sys.path: # Mostramos las rutas de python
  print(i)


print(f"\n[+] Saliendo con un código de estado 1 (no exitoso)")
sys.exit(1) # Obligamos que el código de estado sea 1
