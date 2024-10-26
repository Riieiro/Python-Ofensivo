#!/usr/bin/env python3

class Libro: # Creamos la clase Libro

  def __init__(self, id_libro,autor,nombre_libro): # Constructor con los valores de cada libro

    self.id_libro=id_libro
    self.autor=autor
    self.nombre_libro=nombre_libro
    self.esta_prestado=False # Atributo booleano False por defecto

  def __repr__(self): # Método especial

    return f"Libro ({self.id_libro}, {self.autor}, {self.nombre_libro})" 


class Biblioteca: # Creamos la clase Biblioteca

  def __init__(self): # Constructor sin añadir valores

    self.libros = {} # {1: Libro (1, "Javier Rieiro", "Harry Potter"), 2: Libro(2, "Pepito Manolete","Aprende a colorear desde cero")}

  def agregar_libro(self, libro): # Creamos la función agregar_libro, pasandole el objeto como valor

    if libro.id_libro not in self.libros: # Si el id_libro del objeto que hemos pasado no se encuentra en el diccionario
      self.libros[libro.id_libro] = libro # Añadimos el objeto
    else :
      print (f"\n[!] No es posible agregar el libro con ID {libro.id_libro}")

  def prestar_libro(self,id_libro):
    if id_libro in self.libros and not self.libros[id_libro].esta_prestado: # Si id_libro se encuentra en el diccionario y si el objeto que corresponde a id_libro no esta prestado
      self.libros[id_libro].esta_prestado=True
    else:
      print(f"\n[!] No es posible prestar el libro con ID {id_libro}")

  @property # Creamos una propiedad
  def mostrar_libros(self): # Creamos la función mostrar_libros
    return [libro for libro in self.libros.values() if not libro.esta_prestado] # Para el objeto en el valor del diccionario devolver el objeto si no está prestado

  @property # Creamos una propiedad
  def mostrar_libros_prestados(self): # Creamos la función mostrar_libros_prestados
    return [libro for libro in self.libros.values() if libro.esta_prestado] # Para el objeto en el valor del diccionario devolver el objeto si está prestado


class BibliotecaInfantil(Biblioteca): # Creamos una clase llamada BibliotecaInfantil heredando la clase principal Biblioteca

  def __init__(self): # Creamos el constructor
    super().__init__() # De esta forma hacemos referencia al constructor de la clase principal para no sobreescribirlo
    self.libros_infantiles= {} # {1: False, 2: True}

  def agregar_libro(self,libro, es_infantil): # Usamos la función agregar_libro ya creada añadiendole un nuevo valor

    super().agregar_libro(libro) # Con super hacemos referencia a la función de la clase principal para no sobreescribirla
    self.libros_infantiles[libro.id_libro]= es_infantil # Añadimos al diccionario un valor objeto.id_libro y una clave es_infantil

  def prestar_libro(self,id_libro,es_infantil):
    if id_libro in self.libros and self.libros_infantiles[id_libro] == es_infantil and not self.libros[id_libro].esta_prestado:
# Si id_libro se encuentra en el diccionario (Principal), si el valor pasado es igual a es_infantil en el diccionario (Infantil)
# y si el objeto que corresponde a id_libro en el diccionario (Pricipal)no esta prestado
      self.libros[id_libro].esta_prestado=True
    else:
      print(f"\n[!] No es posible prestar el libro con ID {id_libro}")

  @property
  def mostrar_libros_estado(self):
    return self.libros_infantiles


"""
La sentencia if __name__ == '__main__': es una forma común de controlar si un script está siendo ejecutado directamente o está siendo importado como un módulo en otro script.
Esto permite que ciertas partes del código se ejecuten solo cuando el archivo es ejecutado directamente, y no cuando se está utilizando como parte de otro programa.
"""

if __name__ == '__main__':

  biblioteca=Biblioteca()

  libro1 = Libro(1,"Javier Rieiro", "Harry Potter")
  libro2= Libro(2,"Pepito Manolete","Aprende a colorear desde cero")

  biblioteca.agregar_libro(libro1)
  biblioteca.agregar_libro(libro2)

  print(f"\n[+] Libros en la biblioteca: {biblioteca.mostrar_libros}")

  biblioteca.prestar_libro(1)
  biblioteca.prestar_libro(1)
  print(f"\n[+] Libros en la biblioteca: {biblioteca.mostrar_libros}")
  print(f"\n[+] Libros prestados: {biblioteca.mostrar_libros_prestados}")


  biblioteca_infantil=BibliotecaInfantil()
  biblioteca_infantil.agregar_libro(libro1,es_infantil="False")
  biblioteca_infantil.agregar_libro(libro2,es_infantil="True")
  biblioteca_infantil.prestar_libro(2,es_infantil="True")
  print(f"\n[+] Libros en la biblioteca infantil: {biblioteca_infantil.mostrar_libros_estado}")
  print(f"\n[+] Libros prestados en la biblioteca infantil: {biblioteca_infantil.mostrar_libros_prestados}")
