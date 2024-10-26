#!/usr/bin/env python3

"""
[!] Condicionales

Los condicionales son estructuras de control que permiten ejecutar diferentes bloques de código dependiendo de si una o más condiciones son verdaderas o falsas. En Python, las declaraciones condicionales más comunes son ‘if‘, ‘elif‘ y ‘else‘.

    - if: Evalúa si una condición es verdadera y, de ser así, ejecuta un bloque de código.
    - elif: Abreviatura de “else if“, se utiliza para verificar múltiples expresiones sólo si las anteriores no son verdaderas.
    - else: Captura cualquier caso que no haya sido capturado por las declaraciones ‘if‘ y ‘elif‘ anteriores.

"""



"""
[?] Condicional con 2 condiciones y un else
"""
edad = 20
if edad < 13:
	print("[+] Eres un crío")
elif 13 <= edad < 18:
	print("[+] Eres un adolescente")
else:
	print("[+] Eres un adulto")

# Operador ternario
"""
[?] Condicional al crear una variable
"""
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)

"""
[?] Condicional con dos condiciones
"""
nacionalidad="española"
if edad >= 18 and nacionalidad == "española":
	print("\t[+] Puedes votar en España")
else:
	print("\t[+] No puedes votar")

"""
[?] Condicional con dos posibles condiciones
"""
if edad >= 18 or nacionalidad == "española":
	print ("\t[+] Tienes 18 años o nacionalidad española")
else:
	print("\t[+] No tienes 18 años o nacionalidad española")


"""
[?] Condicional sobre una lista
"""
mi_lista = [1, 4, 6, 12, 14, 18]
if 18 in mi_lista:
	print("El número está en la lista")
else:
	print("El número no está en la lista")

# Condicional anidado
"""
[+] Al cumplir la primera condición, pasas a otra condición
"""
if edad >= 18:
	if nacionalidad=="española":
		print(f"Eres mayor de edad y tienes nacionalidad {nacionalidad}")
	else:
		print("Eres mayor de edad pero no tienes nacionalidad española")
else:
	if nacionalidad=="española":
        	print(f"Eres menor de edad y tienes nacionalidad {nacionalidad}")
	else:
        	print("Eres menor de edad pero no tienes nacionalidad española")


"""
[+] Mini ejercicio para averiguar los números pares
"""
numbers=[1, 2, 3 ,4 ,5 ,6, 7, 8, 9, 10]
for i in numbers:
	if i%2==0:
		print(f"[+] El número {i} es par")





