#!/usr/bin/env python3


"""
[!] Bucles

Los bucles permiten ejecutar un bloque de código repetidamente mientras una condición sea verdadera o para cada elemento en una secuencia. Los dos tipos principales de bucles 
que utilizamos en Python son ‘for‘ y ‘while‘.

    - for: Se usa para iterar sobre una secuencia (como una lista, un diccionario, una tupla o un conjunto) y ejecutar un bloque de código para cada elemento de la secuencia.
    - while: Ejecuta un bloque de código repetidamente mientras una condición específica se mantiene verdadera.

"""
"""
[!] Control de Flujo en Bucles

Existen declaraciones de control de flujo que pueden modificar el comportamiento de los bucles, como ‘break‘, ‘continue‘ y ‘pass‘.

    - break: Termina el bucle y pasa el control a la siguiente declaración fuera del bucle.
    - continue: Omite el resto del código dentro del bucle y continúa con la siguiente iteración.
    - pass: No hace nada, se utiliza como una declaración de relleno donde el código eventualmente irá, pero no ha sido escrito todavía.

"""




"""
[?] Bucle con rango
"""
for i in range(5):
	print(i)

"""
[?] Bucle sobre una lista
"""
names = ["Jose", "Perez", "Gomez"]
for i in names:
 	print(f"[+] El nombre para esta vuelta es {i}")
"""
[?] Bucle while con un contador
"""
i = 0
while i < 5:
	print(i)
	i+=1

"""
[?] Uso de enumerate para mostrar el índice de la lista y el valor
"""
names = ["Jose", "Perez", "Gomez"]
for i, nombre in enumerate(names):
	print(f"[+] Nombre {i+1}: {nombre}")

"""
[?] Bucle sobre un diccionario
"""
frutas = {"manzanas": 1, "peras": 3, "platanos": 4}
for i, c in frutas.items():
	print(f"[+] Hay {c} {i}")

# Bucles anidados
"""
[?] Creamos varias listas y hacemos un primer bucle donde itere por cada lista y otro segundo bucle dentro del primero para iterar sobre el contenido de cada lista
"""
my_list = [[1, 4, 5, 6], [2, 6, 8], [9, 4, 1]]
for i in my_list:
	print(f"\n[+] Vamos a desglosar la lista {i}")
	for j in i:
		print(f"\t--> {j}")

# Lista de compresión (for)
"""
[?] Creamos una lista en la que el contenido sea un bucle for que por cada iteración haga el cuadrado del valor de la lista y lo guarde en la lista cuadrado
"""
odd_list = [1, 3, 5, 7, 9]
cuadrado = [i ** 2 for i in odd_list]
print(cuadrado)


"""
[?] Bucle con rango con uso de break
"""
for i in range(10):
	if i==5:
		break # Finaliza
	print(i)

"""
[?] Bucle con rango con uso de continue
"""
for i in range(10):
	if i==5:
		continue # Salta
	print(i)
"""
[?] Bucle con rango con uso de un condicional if else
"""
for i in range(10):
	if i==5:
		print(f"[+] Actualmente i vale {i}")
	else:
		print(f"[+] Actualmente i no vale 5, sino que vale {i}")

"""
[?] El else se activa cuando el bucle ha finalizado su condición principal, es decir range(10)
"""
for i in range(10):
        if i==15:
                break # Finaliza
        print(i)

else:
	print("[+] Bucle concluido exitosamente")


"""
[?] Como el bucle ha finalizado antes de tiempo no se activa el else
"""
for i in range(10):
        if i==5:
                break # Finaliza
        print(i)
else:
	print("[+] Bucle no concluido")

"""
[?] Mismo ejemplo anterior pero con while
"""
i = 0
while i<10:
	if i == 15:
		print("Salimos antes de tiempo")
		break
	i+=1
else:
	print("[+] Bucle concluido exitosamente")


