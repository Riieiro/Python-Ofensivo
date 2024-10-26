#!/usr/bin/env python3

"""
[!]Funciones Lambda

Las funciones lambda son también conocidas como funciones anónimas debido a que no se les asigna un nombre explícito al definirlas.
Se utilizan para crear pequeñas funciones en el lugar donde se necesitan, generalmente para una operación específica y breve.
En Python, una función lambda se define con la palabra clave ‘lambda‘, seguida de una lista de argumentos, dos puntos y la expresión que desea evaluar y devolver.

Una de las ventajas de las funciones lambda es su simplicidad sintáctica, lo que las hace ideal para su uso en operaciones que requieren una función por un breve momento
 y para casos donde la definición de una función tradicional completa sería excesivamente verbosa.
"""

"""
[!] Usos comunes de las Funciones Lambda

    - Con funciones de orden superior: Como aquellas que requieren otra función como argumento, por ejemplo, ‘map()‘, ‘filter()‘ y ‘sorted()‘.
    - Operaciones simples: Para realizar cálculos o acciones rápidas donde una función completa sería innecesariamente larga.
    - Funcionalidad en línea: Cuando se necesita una funcionalidad simple sin la necesidad de reutilizarla en otro lugar del código.

"""
mi_funcion = lambda : "Hola mundo"
print(mi_funcion())


suma = lambda x,y: x+y
print(suma(10,5))


"""
[?] La función map debe recibir dos parámetros. El primero es la función lambda que hace el cuadrado de un número. El segundo es el número por el cual queremos que itere (En este caso la lista)
    Por último, tranformamos el objeto map a una lista.
"""
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))

print(cuadrados)


"""
[?] La función filter debe recibir dos parámetros. El primero es la función lambda que verifica los números pares. El segundo es el número por el cual queremos que itere (En este caso la lista)
    La función filter muestra los números los cuales son True
    Por último, transformamos el objeto en una lista.
"""
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

"""
[?] La funcion reduce importada del módulo functools, permite múltiplicar el 1 por el 2 y el total de esa operación multiplicarlo por el 3, así hasta el final de la lista
"""
from functools import reduce
producto = reduce(lambda x,y: x*y, numeros)
print(producto)
