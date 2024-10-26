#!/usr/bin/env python3

"""
[!] Clases [!]

Las clases son los fundamentos de la POO. Actúan como plantillas para la creación de objetos y definen atributos y comportamientos que los objetos creados a partir de ellas tendrán. 
En Python, una clase se define con la palabra clave ‘class‘ y proporciona la estructura inicial para todo objeto que se derive de ella.
"""

class Persona:

  def __init__(self,nombre,edad): # Persona.__init__(javi,nombre,edad)

    self.nombre = nombre
    self.edad = edad

  def saludo(self): # Persona.saludo(javi)

    return f"Hola, soy {self.nombre} y tengo {self.edad} años"

javi= Persona("Javi", 19)
juan = Persona("Juan", 21)

print(javi.saludo())
print(juan.saludo())


class Animal:

  def __init__(self,nombre,animal): # Animal.__init__(gato,nombre,animal)

    self.nombre= nombre
    self.animal = animal

  def descripcion(self): # Animal.descripcion(objeto)

    print(f"{self.nombre} es un {self.animal}")

gato= Animal("Mau", "Gato")
perro= Animal("Pancho", "Perro")

gato.descripcion()
perro.descripcion()


class CuentaBancaria:

  def __init__(self,cuenta,nombre,dinero=0):

    self.cuenta = cuenta
    self.nombre = nombre
    self.dinero = dinero

  def depositar_dinero(self, ingreso): # CuentaBancaria.depositar_dinero(objeto(ingreso))

    self.dinero= self.dinero + ingreso
    return f"\n[+] Se han depositado {ingreso}€, actualmente el balance de la cuenta es de {self.dinero}€"

  def retirar_dinero(self, retiro): # CuentaBancaria.retirar_dinero(objeto(retiro))
    
    if retiro < self.dinero:
      self.dinero= self.dinero - retiro
      return f"\n[+] Se han retirado {retiro}€, actualmente el balance de la cuenta es de {self.dinero}€"
    else:
      return f"\n[!] No tienes tanta cantidad, el balance de la cuenta es {self.dinero}"

manolo = CuentaBancaria("1331V13", "Javier Rieiro", 2000)
print(manolo.depositar_dinero(200))
print(manolo.depositar_dinero(500))

print(manolo.retirar_dinero(1000))


"""
[!] Decoradores [!]

Los decoradores son una herramienta poderosa en Python que permite modificar el comportamiento de una función o método. 
Funcionan como “envoltorios”, que agregan funcionalidad antes y después del método o función decorada, sin cambiar su código fuente. 
En POO, los decoradores son frecuentemente utilizados para agregar funcionalidades de manera dinámica a los métodos, como la sincronización de hilos, la memorización de resultados o la verificación de permisos.
"""

class Rectangulo:

  def __init__(self,ancho,alto): # Constructor de los objetos
    self.ancho=ancho
    self.alto=alto

  @property # Decorador para que cuando hagamos print del objeto tenga contenido
  def area(self): # Rectangulo.area(rect1)
    return self.ancho * self.alto

  def __str__(self): # Retorna un string, para poder imprimirlo como si fuera una variable

    return f"\n[+] Propiedades del rectángulo : [Ancho: {self.ancho}] [Alto: {self.alto}]"


  def __eq__(self,otro): # Pone una condición y nos devuelve un boolean

    return self.ancho == otro.ancho and self.alto == otro.alto




rect1=Rectangulo(20,80)
rect2=Rectangulo(20,80)

print(rect1)
print(f"\n[+] El área es {rect1.area}")
print(f"\n[+] ¿Son iguales? -> {rect1 == rect2}")


class Libro:

  IVA = 0.21

  def __init__(self,titulo,autor,precio):

    self.titulo = titulo
    self.autor = autor
    self.precio = precio

  @staticmethod  # Decorador para no jugar con objetos, es decir significa que se puede llamar al método directamente en la clase, sin necesidad de crear una instancia de la misma
                 #Son útiles cuando queremos realizar alguna funcionalidad que está relacionada con la clase, pero que no requiere acceder a la instancia o a los atributos de la clase.
  def es_bestseller(total_ventas): # Libro.es_bestseller(mi_libro,total_ventas)

    return total_ventas > 5000
  @classmethod # Decorador para que dependa de la clase, si tienes una clase heredada de esta forma no influye en las dos 
               # Los métodos de clase son utilizados a menudo para definir métodos “factory” que pueden crear instancias de la clase de diferentes maneras.
  def precio_con_iva(cls, precio):

    return precio + precio * cls.IVA

mi_libro = Libro("Spiderman","Javier Rieiro",20.5)
print(Libro.es_bestseller(700))

print(f"\n[+] El precio del libro con IVA incluido es de {mi_libro.precio_con_iva(mi_libro.precio)}")











