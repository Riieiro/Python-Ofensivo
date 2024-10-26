#!/usr/bin/env python3
"""
[!] Funciones

Las funciones son bloques de código reutilizables diseñados para realizar una tarea específica.
En Python, se definen usando la palabra clave ‘def‘ seguida de un nombre descriptivo, paréntesis que pueden contener parámetros y dos puntos.
Los parámetros son “variables de entrada” que pueden cambiar cada vez que se llama a la función.
Esto permite a las funciones operar con diferentes datos y producir resultados correspondientes.

Las funciones pueden devolver valores al programa principal o a otras funciones mediante la palabra clave ‘return‘.
Esto las hace increíblemente versátiles, ya que pueden procesar datos y luego pasar esos datos modificados a otras partes del programa
"""

def saludo(nombre):
	print(f"\nHola {nombre}")

saludo("Pepe")


def suma(x, y):
	return x+y

resultado = suma(2, 5)
print(f"[+] La suma de ambos valores es {resultado}")

"""
[!] Ámbito de las Variables (Scope)

El ámbito de una variable se refiere a la región de un programa donde esa variable es accesible. En Python, hay dos tipos principales de ámbitos:

    - Local: Las variables definidas dentro de una función tienen un ámbito local, lo que significa que solo pueden ser accesadas y modificadas dentro de la función donde fueron creadas.
    - Global: Las variables definidas fuera de todas las funciones tienen un ámbito global, lo que significa que pueden ser accesadas desde cualquier parte del programa.
              Sin embargo, para modificar una variable global dentro de una función, se debe declarar como global.

"""


"""
[?] Al crear una variable dentro de una función, python no reconoce esta variable fuera de la función
"""
def mi_funcion():
	variable_local = "Soy una variable local"
	print(variable_local)

mi_funcion()

"""
[?] En este ejemplo vemos como funciona el ámbito de las variables. Primero creamos a nivel global la variable y después creamos a nivel local otra variable con el mismo nombre
    De esta forma vemos que las variables locales y globales no tienen ninguna relación, aunque tengan el mismo nombre 
"""
variable = "Soy global"

def ejemplo():
	variable = "Soy local"
	print(variable)
ejemplo()
print(variable)

"""
[?] Sin embargo, las variables globales si pueden ser interpretadas en una función
"""
variable = "Soy global"
def ejemplo2():
	print(variable)
ejemplo2()
print(variable)

"""
[?] Para cambiar el contenido de la variable a nivel global dentro de una función podemos hacerlo así
"""
variable = "Soy global"
def ejemplo2():
	global variable
	variable = "Soy global y he sido modificado"
	print(variable)
ejemplo2()
print(variable)



















