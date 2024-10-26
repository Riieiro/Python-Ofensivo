#!/usr/bin/env

"""
[!] Decoradores [!]

Los decoradores en Python son una forma elegante de modificar las funciones o métodos.
Se utilizan para extender o alterar el comportamiento de la función sin cambiar su código fuente.
Un decorador es en sí mismo una función que toma otra función como argumento y devuelve una nueva función que, opcionalmente,
puede agregar alguna funcionalidad antes y después de la función original.

[!] Propiedades [!]

Las propiedades son un caso especial de decoradores que permiten a los desarrolladores añadir “getter“, “setter” y “deleter”
a los atributos de una clase de manera elegante, controlando así el acceso y la modificación de los datos.
En Python, esto se logra con el decorador ‘@property‘, que transforma un método para acceder a un atributo como si fuera un atributo público.

[!] Getters y Setters [!]

    - El “getter” obtiene el valor de un atributo manteniendo el encapsulamiento y permitiendo que se ejecute una lógica adicional durante el acceso.
    - El “setter” establece el valor de un atributo y puede incluir validación o procesamiento antes de que el cambio se refleje en el estado interno del objeto.
    - El “deleter” puede ser utilizado para definir un comportamiento cuando un atributo es eliminado con del.
"""



def mi_decorador(funcion): # Función de orden superior
    def envoltura():
        print("Estoy saludando en la envoltura del decorador antes de la función")
        funcion() # LLamada a la función original
        print("Estoy saludando en la envoltura del decorador después de llamar a la función")
    return envoltura


@mi_decorador
def saludo():

    print("Hola, estoy saludando dentro de la función")

saludo()



class Persona:

    def __init__(self,nombre,edad):

        self._nombre=nombre
        self._edad=edad

    @property
    def edad(self): # Creación Getter
        return self._edad

    @edad.setter # Creación Setter (De esta forma tenemos un mayor control de los valores protegidos que añadimos fuera del programa)
    def edad(self,valor):
        if valor>0:
            self._edad=valor
        else:
            raise ValueError("[!] La edad no puede ser un número negativo")

manolo = Persona("Manolo",23)
manolo.edad=14 # Setter
print(manolo._edad) # Getter


import time

def cronometro(funcion):
    def envoltura():
        inicio=time.time()
        funcion()
        final=time.time()

        print(f"Tiempo total transcurrido en la funcion {funcion.__name__}: {final-inicio}")
    return envoltura

@cronometro
def pausa_corta():
    time.sleep(1)

@cronometro
def pausa_larga():
    time.sleep(2)

pausa_corta()
pausa_larga()


def suma(*args): # La función *args crea una tupla con todos los valores proporcionados
    return sum(args)

print(suma(2,3,4,5,6,3,42,12))


def presentacion(**kwargs): # La función **kwargs crea un diccionario con todos los valores proporcionados
    print(kwargs)

    for clave,valor in kwargs.items():
        print(f"{clave}: {valor}")

presentacion(nombre="Javier", edad=19, ciudad="Madrid", profesion="Estudiante")

# [i] Si utilizas las dos funciones python clasifica los valores pudiendo crear una tupla y un diccionario



class Circunferencia:

    def __init__(self,radio):
        self._radio=radio

    @property
    def radio(self): # Creamos Getter
        return self._radio

    @property
    def diametro(self):
        return 2*self._radio

    @property
    def area(self):
        return 3.1415 * (self._radio ** 2)

    @radio.setter # Creamos Setter
    def radio(self,valor):
        self._radio=valor

c=Circunferencia(5)
print(c.radio)
print(c.diametro)
print(c.area)

c.radio=10
print(c.radio)
print(c.diametro)
print(c.area)



