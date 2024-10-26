#!/usr/bin/env python3

"""
[!] Algunos métodos especiales importantes en POO son: [!]

    __init__(self, […]): Inicializa una nueva instancia de la clase.
    __str__(self): Devuelve una representación en cadena de texto del objeto, invocado por la función ‘str(object)‘ y ‘print‘.
    __repr__(self): Devuelve una representación del objeto que debería, en teoría, ser una expresión válida de Python, invocado por la función ‘repr(object)‘.
    __eq__(self, other): Define el comportamiento del operador de igualdad ‘==‘.
    __lt__(self, other), __le__(self, other), __gt__(self, other), __ge__(self, other): Definen el comportamiento de los operadores de comparación (<, <=, > y >= respectivamente).
    __add__(self, other), __sub__(self, other), __mul__(self, other), etc.: Definen el comportamiento de los operadores aritméticos (+, –, *, etc.).


[!] Atributos Públicos [!]

Son accesibles desde cualquier parte del programa y, por convención, no tienen un prefijo especial. Se espera que estos atributos sean parte de la interfaz permanente de la clase.


[!] Atributos Protegidos [!]

Se indica con un único guion bajo al principio del nombre (por ejemplo, ‘_atributo‘). 
Esto es solo una convención y no impide el acceso desde fuera de la clase, pero se entiende que estos atributos están protegidos y no deberían ser accesibles directamente, excepto dentro de la propia clase y en subclases.


[!] Atributos Privados [!]

En Python, los atributos privados se indican con un doble guion bajo al principio del nombre (por ejemplo, ‘__atributo‘). 
Esto activa un mecanismo de cambio de nombre conocido como ‘name mangling‘, donde el intérprete de Python altera internamente el nombre del atributo para hacer más difícil su acceso desde fuera de la clase.
"""



class Ejemplo:

  def __init__(self):

    self._atributo_protegido="Soy un atributo protegido y no deberías poder verme" # Atributo protegido
    self.__atributo_privado="Soy un atributo privado y no deberías poder verme" # Atributo privado name manglin(Añade un _Ejemplo al inicio)

ejemplo=Ejemplo()
print(ejemplo._atributo_protegido)
print(ejemplo._Ejemplo__atributo_privado)


class Coche:

  def __init__(self,marca,modelo):

    self.marca=marca
    self.modelo=modelo
    self.__kilometraje=0 # Atributo privado

  def conducir(self,kilometros):

    if kilometros >= 0:

      self.__kilometraje+=kilometros

    else:

      print("\n[!] Los kilómetros deben ser mayores a 0\n")

  def mostrar_kilometros(self):

    return self.__kilometraje


coche = Coche("Toyota","Corolla")
coche.conducir(150)
print(coche.mostrar_kilometros())


class Libro:

  def __init__(self,autor,titulo):

    self.autor=autor
    self.titulo=titulo

  def __str__(self):

    return f"El libro {self.titulo} ha sido escrito por {self.autor}"

  def __eq__(self,otro):

    return self.autor==otro.autor and self.titulo==otro.titulo


mi_libro = Libro("Javi","Harry Potter")
mi_libro2 = Libro("Javi","Harry Potter")

print(mi_libro)
print(f"Son iguales --> {mi_libro==mi_libro2}")


class CuentaBancaria:

  def __init__(self,num_cuenta,titular,saldo_inicial=0):

    self.num_cuenta=num_cuenta
    self.titular=titular
    self.__saldo = saldo_inicial

  def depositar_dinero(self,cantidad):

    if cantidad > 0:
      self.__saldo +=cantidad
      print(f"Saldo -> {self.__saldo}")
    else:

      print("[!] Error")



  def retirar_dinero(self,cantidad):
    if cantidad > 0:
      if cantidad > self.__saldo:
        print("[!] Error")
      else:
        self.__saldo -=cantidad
        print(f"Saldo -> {self.__saldo}")
    else:
      print("[!] Error")





manolo = CuentaBancaria("24242","Manolo Vieira")

manolo.depositar_dinero(500)
manolo.retirar_dinero(19)


class Caja:

  def __init__(self, *items): # Creamos una tupla

    self.items=items

  def mostrar_items(self):

    for i in self.items:
      print(i)

  def __len__(self): # Función especial para poder hacer un len de la tupla

    return len(self.items)


caja=Caja ("Manzana","Platano","Kiwi","Pera")

caja.mostrar_items()
print(len(caja))


class Pizza:

  def __init__(self,size,*ingredientes):

    self.size=size
    self.ingredientes=ingredientes

  def descripcion(self):

    print(f"[i] Esta pizza tiene {self.size} cm de longitud y los ingredientes son: {', '.join(self.ingredientes)}")


pizza = Pizza(23,"Bacon","Queso","Tomate")
pizza.descripcion()


class Mi_lista:

  def __init__(self):

    self.data=[1,2,3,4,5]

  def __getitem__(self,index): # Metodo especial para poder filtrar por indice en la lista que indiquemos

    return self.data[index]

lista= Mi_lista()
print(lista[2])


class Saludo:

  def __init__(self,saludo):

    self.saludo=saludo

  def __call__(self,nombre):

    return f"{self.saludo} {nombre}!"


hola=Saludo("¡Hola")
print(hola("Luis"))


class Punto:

  def __init__(self,x,y):

    self.x=x
    self.y=y

  def __add__(self,otro): # Metodo especial para sumar dos objetos

    return Punto(self.x+otro.x, self.y+otro.y) # Objeto temporal

  def __str__(self):

    return f"({self.x}, {self.y})"


p1 =Punto(2,8)
p2=Punto(4,9)

print(p1+p2) # (6,17)


class Contador:

  def __init__(self,limite):

    self.limite=limite

  def __iter__(self): # Metodo especial para devolver un iterador

    self.contador=0

    return self

  def __next__(self): # Metodo especial para devolver que tiene que hacer el bucle en cada iteracion

    if self.contador < self.limite:  # Ponemos una condición como en los bucles while
      self.contador+=1
      return self.contador
    else:
      raise StopIteration

c = Contador(5)

for i in c:
  print(i)
