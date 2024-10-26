"""
[!] Estructura de Módulos [!]

Cada módulo en Python es un archivo ‘.py‘ que encapsula tu código para un propósito específico.
Por ejemplo, puedes tener un módulo para operaciones matemáticas, otro para manejo de entradas/salidas,
y otro para la lógica de la interfaz de usuario. Esta estructura ayuda a mantener el código organizado, facilita la lectura y hace posible la reutilización de código. 


[!] Importación de Módulos [!]

Python utiliza la palabra clave ‘import‘ para utilizar módulos.
Puedes importar un módulo completo, como ‘import math‘, o importar nombres específicos de un módulo utilizando ‘from math import sqrt‘.
Python también permite la importación de módulos con un alias para facilitar su uso dentro del código, como ‘import numpy as np‘.


[!] Paquetes [!]

Cuando los programas crecen y los módulos comienzan a acumularse, Python permite organizar módulos en paquetes.
Un paquete es una carpeta que contiene módulos y un archivo especial llamado ‘__init__.py‘, que indica a Python que esa carpeta contiene módulos que pueden ser importados.

[!] Ventajas de los Módulos [!]

    - Mantenimiento: Los módulos permiten trabajar en partes del código de manera independiente sin afectar otras partes del sistema.
    - Espacio de Nombres: Los módulos definen su propio espacio de nombres, lo que significa que puedes tener funciones o clases con el mismo nombre en diferentes módulos sin conflicto.
    - Reutilización: El código escrito en módulos puede ser reutilizado en diferentes programas simplemente importándolos donde se necesiten.

"""



import math_operation

print(math_operation.suma(5,6))

# Otra forma de importar módulos:

"""
from math_operation import suma,resta,multiplicacion,division

print(suma(5,6))
"""
# Existen varios módulos que pertenecen directamente al intérprete de python, estos módulos no son archivos .py. Para ver estos módulos podemos hacer esto:
import sys
print(sys.builtin_module_names)

import math
from math import * # De esta forma importamos todas las funciones del módulo math

print(dir(math)) # De esta forma vemos todas las funciones que tiene el módulo math
print(sqrt(16))
