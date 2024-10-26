#!/usr/bin/env python3

class Nota: # Creamos la clase Nota

  def __init__(self,contenido): # En el constructor le pasamos una varible contenido

    self.contenido=contenido

  def coincide(self,texto_busqueda): # Creamos la función coincide pasandole la variable indicada en el archivo main
    return texto_busqueda in self.contenido # Devuelve un booleano dependiendo de si la variable texto_busqueda se encuentra en el contenido de la nota

  def __str__(self):
    return self.contenido
