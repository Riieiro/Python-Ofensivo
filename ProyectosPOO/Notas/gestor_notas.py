#!/usr/bin/env python3

import pickle # Importamos la librería pickle para emplear la serialización del contenido
from notas import Nota # Importamos la clase Nota del archivo notas creado por nosotros

class GestorNotas: # Creamos la clase GestorNotas

  def __init__(self, archivo_notas='notas.pkl'): # En el constructor creamos una variable con el nombre del archivo por defecto. 
                                                 # De esta forma al crear el objeto en el archivo main se creará por defecto el nombre del archivo notas.pkl

    self.archivo_notas=archivo_notas

    try: # Prueba a abrir el archivo notas.pkl, si lo puede abrir significa que el archivo ya tiene contenido
      with open(self.archivo_notas, 'rb') as f:
        self.notas = pickle.load(f) # Guardamos el archivo notas.pkl en la lista notas que en este caso ya a sido creada
                                          # Con este try/except identificamos si el archivo notas.pkl ya tiene contenido
    except FileNotFoundError: # Si no consigue abrir el archivo crea una nueva lista vacía
      self.notas=[] # Al usar el formato de listas estamos guardando el contenido en modo lineal

  def guardar_notas(self): # Creamos la función guardar_notas para tener controlado el contenido de las notas

    with open(self.archivo_notas, 'wb') as f: # Abrimos el archivo notas.pkl con permisos de escritura en binario
      pickle.dump(self.notas, f) # De esta forma almacenamos el contenido de la lista notas en un el archivo notas.pkl

  def agregar_nota(self,contenido): # Creamos la función agregar_nota recibiendo la variable contenido

    self.notas.append(Nota(contenido)) # Almacenamos el contenido en la lista notas llamando a la clase Nota del archivo notas | Esto crea una especie de objeto temporal
    self.guardar_notas() # Llamamos a la función guardar_notas

  def leer_notas(self): # Creamos la función leer_notas
    return self.notas # Retornamos la lista

  def buscar_nota(self,texto_busqueda): # Creamos la función buscar_nota, pasandole la variable texto_busqueda del archivo main
    return [nota for nota in self.notas if nota.coincide(texto_busqueda)] # Retornamos el siguiente bucle: Itera por cada valor de la lista y devuelve ese valor si la función coindide
                                                                          # del archivo notas devuelve un estado booleano True

  def eliminar_nota(self,index): # Creamos la función eliminar_nota recibiendo la variable index
    if index < len(self.notas): # Si el número indicado es mayor que número de notas que hay en la lista
      del self.notas[index] # Borra la nota del índice indicado de la lista notas
      self.guardar_notas() # Llamamos a la función guardar_notas para sobreescribir el archivo notas.pkl
    else:
      print("\n[!] El índice proporcionado no es correcto ")

  def vaciar_notas(self): # Creamos la función vaciar_notas
    self.notas.clear() # Vaciamos la lista notas


