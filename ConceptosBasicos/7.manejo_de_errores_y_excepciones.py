#!/usr/bin/env python3

"""
[!] Manejo de Errores [!]

Los errores pueden ocurrir por muchas razones: errores de código, datos de entrada incorrectos, problemas de conectividad, entre otros. 
En lugar de permitir que un programa falle con un error, Python nos proporciona herramientas para ‘atrapar’ estos errores y manejarlos de manera controlada,
evitando así que el programa se detenga inesperadamente y permitiendo reaccionar de manera adecuada.

[!] Excepciones [!]

Una excepción en Python es un evento que ocurre durante la ejecución de un programa que interrumpe el flujo normal de las instrucciones del programa. 
Cuando el intérprete se encuentra con una situación que no puede manejar, ‘levanta’ o ‘arroja’ una excepción.


[!] Bloques try y except [!]

Para manejar las excepciones, utilizamos los bloques ‘try‘ y ‘except‘. Un bloque ‘try‘ contiene el código que puede producir una excepción,
mientras que un bloque ‘except‘ captura la excepción y contiene el código que se ejecuta cuando se produce una.

[!] Otras Palabras Clave de Manejo de Excepciones [!]

    - else: Se puede usar después de los bloques ‘except‘ para ejecutar código si el bloque ‘try‘ no generó una excepción.
    - finally: Se utiliza para ejecutar código que debe correr independientemente de si se produjo una excepción o no, como cerrar un archivo o una conexión de red.


[!] Levantar Excepciones [!]

También es posible ‘levantar’ una excepción intencionalmente con la palabra clave ‘raise‘, lo que permite forzar que se produzca una excepción bajo condiciones específicas.
"""



try:
	num = 5/0
except ZeroDivisionError:
	print("[!] No se puede dividir un número entre cero")
except TypeError:
	print("[!] Solo es posible dividir números enteros")
except NameError:
	print("[!] La operación no es válida")
else: 
	print(f"[!] La división de estos números es {num}")
finally:
	print("[!] Esto siempre se va a ejecutar")

"""
[?] Con raise podemos llamar a la excepción
"""
x=-5 
if x<0:
	raise Exception("No se pueden usar números negativos")


