#!/usr/bin/env python3
"""
[!] Características de las Tuplas [!]

    - Inmutabilidad: Una vez que se crea una tupla, no puedes cambiar, añadir o eliminar elementos. Esta inmutabilidad garantiza la integridad de los datos que desea mantener constantes.
    - Indexación y Slicing: Al igual que las listas, puedes acceder a los elementos de la tupla mediante índices y también puedes realizar operaciones de slicing para obtener subsecuencias de la tupla.
    - Heterogeneidad: Las tuplas pueden contener elementos de diferentes tipos, incluyendo otras tuplas, lo que las hace muy versátiles.


[!] Operaciones con Tuplas [!]

Aunque no puedes modificar una tupla, hay varias operaciones que puedes realizar:

    - Empaquetado y Desempaquetado de Tuplas: Las tuplas permiten asignar y desasignar sus elementos a múltiples variables de forma simultánea.
    - Concatenación y Repetición: Similar a las listas, puedes combinar tuplas usando el operador ‘+‘ y repetir los elementos de una tupla un número determinado de veces con el operador ‘*‘.
    - Métodos de Búsqueda: Puedes usar métodos como ‘index()‘ para encontrar la posición de un elemento y ‘count()‘ para contar cuántas veces aparece un elemento en la tupla.


[!] Uso de Tuplas en Python [!]

    - Funciones y Asignaciones Múltiples: Las tuplas son muy útiles cuando una función necesita devolver múltiples valores o cuando se realizan asignaciones múltiples en una sola línea.
    - Estructuras de Datos Fijas: Se usan para crear estructuras de datos que no deben cambiar, como los días de la semana o las coordenadas de un punto en el espacio.

"""





"""
[?] Las tuplas son inmutables, es decir las funciones pop(),insert()... No funcionan
"""
example = (1, 2, 3,{'manzanas': 1, 'peras': 4}, 4, 5, [1, 2, "test"])

print(type(example))
print(example[-1])



for element in example:
	print(element)
"""
[?] Las tuplas tienen la capacidad de almacenar cada valor en otras variables
"""
mi_tupla = (1, 2, 3, 4)
a, b, c, d = mi_tupla
print(a)
print(b)
print(c)
print(d)
print(len(mi_tupla))

"""
[?] Es posible hacer operaciones con tuplas, siempre creando una nueva tupla, es decir, nunca se modifica una tupla
"""
mi_primera_tupla = (1, 2, 3, 4)
mi_segunda_tupla = (5, 6, 7, 8, 9)
mi_tercera_tupla = mi_primera_tupla + mi_segunda_tupla
print(mi_tercera_tupla)


"""
[?] Creando una nueva tupla podemos hacer operaciones como esta: 
"""
numeros_pares = tuple(i for i in mi_tercera_tupla if i % 2 == 0)
print(numeros_pares)







