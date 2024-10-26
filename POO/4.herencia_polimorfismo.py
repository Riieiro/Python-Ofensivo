#!/usr/bin/env python3

"""
[!] Herencia [!]

Es un principio de la POO que permite a una clase heredar atributos y métodos de otra clase, conocida como su clase base o superclase. 
La herencia facilita la reutilización de código y la creación de una jerarquía de clases. Las subclases heredan las características de la superclase, lo que permite que se especialicen o modifiquen comportamientos existentes.


[!] Polimorfismo [!]

Este concepto se refiere a la habilidad de objetos de diferentes clases de ser tratados como instancias de una clase común. 
El polimorfismo permite que una función o método interactúe con objetos de diferentes clases y los trate como si fueran del mismo tipo, siempre y cuando compartan la misma interfaz o método. 
Esto significa que el mismo método puede comportarse de manera diferente en distintas clases, un concepto conocido como sobrecarga de métodos.

Ambos, la herencia y el polimorfismo, son piedras angulares de la POO y son ampliamente utilizados para diseñar sistemas que son fácilmente extensibles y mantenibles.
"""

class Animal:

  def __init__(self,nombre):

    self.nombre = nombre

  def hablar(self):

     raise NotImplementedError("Las subclases definidads deben implementar este método") # De esta foma mandamos un error por pantalla cuando el desarrollador necesite crear una subclase


class Gato(Animal): # Gato(Animal(gato,nombre))

  def hablar(self):

    return "Miau"

class Perro(Animal):

  def hablar(self):

    return "Guau"

def hacer_hablar(objeto): # Hemos creado una función fuera de las clases, pero reconoce las subclases al llamar a objeto.hablar(). Esto se conoce como polimorfismo

  print(f"{objeto.nombre} dice {objeto.hablar()}")



gato= Gato("Firulais")
perro = Perro("Alfredo")

print(gato.hablar())
print(perro.hablar())

hacer_hablar(gato)
hacer_hablar(perro)

class Automovil:

  def __init__(self,marca,modelo):

    self.marca = marca
    self.modelo = modelo

  def describir(self):

    return f"Vehículo: {self.marca} {self.modelo}"

class Coche(Automovil):

  def describir(self):

    return f"Coche: {self.marca} {self.modelo}"

class Moto(Automovil):

   def describir(self): 

    return f"Moto: {self.marca} {self.modelo}"


def describir_vehiculo(vehiculo):

  print(vehiculo.describir()) # Polimorfismo




coche = Coche("Toyota", "Corolla")
moto= Moto("Honda", "CBR")

print(coche.describir())
print(moto.describir())

describir_vehiculo(coche)
describir_vehiculo(moto)


class Dispositivo:

  def __init__(self,modelo):

    self.modelo=modelo

  def escanear_vulnerabilidades(self):

    raise NotImplementedError("Este método debe ser definido para el resto de subclases existentes")


class Ordenador(Dispositivo):

  def escanear_vulnerabilidades(self):

    return f"[+] Análisis de vulnerabilidades concluido: Múltiples puertos críticos detectados como abiertos"

class TelefonoMovil(Dispositivo):

  def escanear_vulnerabilidades(self):

    return f"[+] Análisis de vulnerabilidades concluido: Múltiples aplicaciones detectadas con permisos excesivos"

class Router(Dispositivo):

  def escanear_vulnerabilidades(self):

    return f"[+] Análisis de vulnerabilidades concluido: Múltiples puertos abiertos"

def escanear_vuln(disp):

  print(disp.escanear_vulnerabilidades())

pc= Ordenador("Dell XPS")
router= Router("Tp-Link Archer")
movil=TelefonoMovil("Iphone 12")


escanear_vuln(pc)
escanear_vuln(router)
escanear_vuln(movil)



class A:

  def __init__(self,x):

    self.x = x
    print(f"Valor en x: {self.x}")

class B(A):

  def __init__(self,x,y):

    self.y = y
    super().__init__(x) # De esta forma, llamamos a la funcion padre
    print(f"Valor en y: {self.y}")


b=B(2,10)


class A:

  def saludo(self):

    return "Saludo A"

class B(A):

  def saludo(self):

    original= super().saludo()
    print(f"{original}, pero tambien saludo desde B")

saludo= B()
saludo.saludo()


class Persona:

  def __init__(self,nombre,edad):

    self.nombre=nombre
    self.edad=edad

  def saludo(self):

    return f"Hola, soy {self.nombre} y tengo {self.edad} años"

class Empleado(Persona):

  def __init__(self,nombre,edad,salario):

    super().__init__(nombre,edad)
    self.salario=salario

  def saludo(self):

    return f"{super().saludo()}, y cobro {self.salario}€ brutos anuales"

persona =Empleado("Alicia",23,3555)
print(persona.saludo())























