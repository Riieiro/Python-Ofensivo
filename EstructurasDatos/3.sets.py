#!/usr/bin/env python3
"""
[!] Características de los Conjuntos [!]

    - Unicidad: Los conjuntos automáticamente descartan elementos duplicados, lo que los hace perfectos para recolectar elementos únicos.
    - Desordenados: A diferencia de las listas y las tuplas, los conjuntos no mantienen los elementos en ningún orden específico.
    - Mutabilidad: Los elementos de un conjunto pueden ser agregados o eliminados, pero los elementos mismos deben ser inmutables (por ejemplo, no puedes tener un conjunto de listas, ya que las listas se pueden modificar).


[!] Operaciones con Conjuntos [!]

Exploraremos las operaciones básicas de conjuntos que Python facilita, como:

    - Adición y Eliminación: Añadir elementos con ‘add()‘ y eliminar elementos con ‘remove()‘ o ‘discard()‘.
    - Operaciones de Conjuntos: Realizar uniones, intersecciones, diferencias y diferencias simétricas utilizando métodos o operadores respectivos.
    - Pruebas de Pertenencia: Comprobar rápidamente si un elemento es miembro de un conjunto.
    - Inmutabilidad Opcional: Usar el tipo ‘frozenset‘ para crear conjuntos que no se pueden modificar después de su creación.


[!] Uso de Conjuntos en Python [!]

    - Eliminación de Duplicados: Son útiles cuando necesitas asegurarte de que una colección no tenga elementos repetidos.
    - Relaciones entre Colecciones: Facilitan la comprensión y el manejo de relaciones matemáticas entre colecciones, como subconjuntos y superconjuntos.
    - Rendimiento de Búsqueda: Proporcionan una búsqueda de elementos más rápida que las listas o las tuplas, lo que es útil para grandes volúmenes de datos.
"""


"""
[?] - add: Añade valores
    - update: Añade 1 o más valores
    - remove: Borra valores, en caso de que ese valor no exista te manda un error
    - discard: Borra valores, en caso de que ese valor no exista no manda error
"""
mi_conjunto = {1, 2, 3}
mi_conjunto.add(8)
mi_conjunto.update({4, 5, 6})
mi_conjunto.remove(6)
mi_conjunto.discard(7)
print(mi_conjunto)


"""
[?] - intersection: Hace una intersección de dos sets
    - union: Hace una unión de dos sets, sin repeticiones
    - difference: Hace la diferencia de dos sets
"""
mi_primer_conjunto= {1, 2, 3, 4, 5}
mi_segundo_conjunto= {3, 4, 5, 6, 7, 5}
conjunto_intersection = mi_primer_conjunto.intersection(mi_segundo_conjunto)
conjunto_union = mi_primer_conjunto.union(mi_segundo_conjunto)
conjunto_difference = mi_primer_conjunto.difference(mi_segundo_conjunto)


"""
[?] - issubset: Comprueba si un conjunto es subconjunto de otro, es decir, que todo el contenido del set se encuentre en el otro set. Esto devuelve un boolean
"""
primer_conjunto= {2, 3, 1}
segundo_conjunto = {1, 2, 3, 4, 5, 9}
print(primer_conjunto.issubset(segundo_conjunto))


"""
[?] Los sets pueden servir para quitar los valores repetidos de una lista, tupla ...
"""
mi_lista = [1, 4, 5, 6, 21, 34, 4, 1, 1, 1, 5, 5]
no_repeat = list(set(mi_lista))
print(no_repeat)


"""
[?] Los sets pueden servir para comprobar si un valor se encuentra en la lista, tupla ...
"""
mi_conjunto = set(range(10000))
print(1234 in mi_conjunto)










