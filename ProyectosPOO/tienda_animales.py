#!/usr/bin/env python3

class Animal: # Creamos clase animal

  def __init__(self,nombre,especie): # Creamos constructor

    self.nombre=nombre
    self.especie=especie
    self.alimentado=False # Creamos un atributo booleano

  def __repr__(self): # Creamos un método especial __repr__ para ofrecer contenido str al objeto

    return f"[+] Nombre --> {self.nombre} | Especie --> {self.especie} - {'Alimentado' if self.alimentado else 'Hambriento'}"

  def alimentar(self): # Creamos una función alimentar en la que pasemos a True el atributo boolenano. Esta función la usaremos más adelante

    self.alimentado=True

  def vender(self):

    self.alimentado=False # Creamos una función vender en la que pasemos a True el atributo booleano. Esta función la usaremos más adelante

class TiendaAnimales: # Creamos clase TiendaAnimales

  def __init__(self,nombre): # Creamos constructor

    self.nombre=nombre
    self.animales = [] # Creamos una lista vacía

  def agregar_animal(self,animal): # Creamos la función agregar_animal, pasandole un valor animal

    self.animales.append(animal) # Con .append() añadimos un valor a la lista

  def mostrar_animales(self): # Creamos la función mostrar_animales

    for animal in self.animales: # Creamos un bucle para iterar sobre cada elemento de la lista

      print(f"{animal}") # Por cada iteración mostramos el objeto animal

  def alimentar_animal(self): # Creamos la función alimentar_animal

    for animal in self.animales: # Creamos un bucle en la que itere por cada valor de la lista 

      animal.alimentar() # Por cada iterción llamamos a la función anteriormente definida alimentar

  def vender_animal(self,nombre): # Creamos la función vender_animal en la que le pasamos un valor nombre

    for animal in self.animales: # Creamos un bucle en la que itere por cada valor de la lista
      if animal.nombre==nombre: # Por cada iteración empleamos una condición en la que si el nombre del objeto animal, coincide con el nombre proporcionado, llame a la función vender
        animal.vender() # De esta forma pasamos a False el atributo booleano
        self.animales.remove(animal) # Indicamos que elimine el objeto animal de la lista
        return # Para parar el bucle una vez encuentre el nombre
    print(f"\n[!] No se ha enconctrado ningún animal en la tienda con nombre {nombre}")

if __name__ == '__main__':


  tienda= TiendaAnimales("Mi tienda de animales")

  gato = Animal("Mau", "Gato")
  perro= Animal("Juan","Perro")

  tienda.agregar_animal(gato)
  tienda.agregar_animal(perro)

  tienda.mostrar_animales()


  tienda.alimentar_animal()
  print("\n")
  tienda.mostrar_animales()
  tienda.vender_animal("Mau")
  print("\n")
  tienda.mostrar_animales()
