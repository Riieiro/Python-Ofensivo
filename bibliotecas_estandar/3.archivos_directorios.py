#!/usr/bin/env python3


import os
import shutil


if os.path.exists("mi_archivo.txt"):  # Comprobar si el archivo mi_archivo.txt existe
  print(f"\n[+] El archivo existe")
else:
  print("\n[!] El archivo no existe")


if not os.path.exists("mi_directorio"): # Comprobar si el directorio mi_directorio existe
  os.mkdir("mi_directorio") # Crear el directorio mi_directorio


if not os.path.exists("mi_directorio/mi_subdirectorio"): # Comprobar si la ruta mi_directorio/mi_subdirectorio existe
  os.makedirs("mi_directorio/mi_subdirectorio") # Crear mi_directorio y mi_subdirectorio


print("\n[+] Listando todos los archivos\n") 
for recursos in os.listdir(): # Iterar por cada archivo | La función os.listdir() devuelve una lista de todos los archivos del directorio actual
  print(recursos)


if os.path.exists("file1.txt"): # Comprobar si el archivo file1.txt existe
  os.remove("file1.txt") # Eliminar el archivo file1.txt


if os.path.exists("prueba"): # Comprobar si el directorio prueba existe
  os.rmdir("prueba") # Eliminar el directorio prueba | NOTA: Esta función solo funciona con directorios vacíos


if os.path.exists("mi_directorio"): # Comprobar si el directorio mi_directorio existe
  shutil.rmtree("mi_directorio") # Eliminar el directorio mi_directorio y su contenido


if os.path.exists("file2.txt"): # Comprobar si el archivo file2.txt existe
  os.rename("file2.txt", "cambiado.txt") # Renombrar el archivo file2.txt por cambiado.txt


if os.path.exists("/etc/passwd"): # Comprobar si el archivo /etc/passwd existe
  tamaño=os.path.getsize("/etc/passwd") # Guardamos en una variable el tamaño en bytes del archivo /etc/passwd
  print(f"\n[+] El archivo /etc/passwd pesa {tamaño} bytes")


ruta = os.path.join("mi_directorio","mi_archivo.txt") # Creamos la ruta mi_directorio/mi_archivo.txt
print(f"\n[+] Ruta: {ruta}")


archivo = os.path.basename(ruta) # De esa ruta almacenamos en una variable el archivo con basename
print(f"\n[+] Nombre del archivo: {archivo}")


directorio= os.path.dirname(ruta) # De esa ruta almacenamos en una variable el directorio con dirname
print(f"\n[+] Nombre del directorio donde está contenido el archivo: {directorio}")


directorio,archivo= os.path.split(ruta) # De esa ruta almacenamos el directorio y el archivo en dos variables diferentes
print(f"[+] Archivo: {archivo}. Directorio: {directorio}")
