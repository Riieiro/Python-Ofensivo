#!/usr/bin/env python3

"""
[!] Características de las Listas [!]

Vamos a explorar las características clave de las listas en Python, que incluyen su capacidad para:

    - Almacenar datos heterogéneos, es decir, pueden contener elementos de diferentes tipos (enteros, cadenas, flotantes y más) dentro de una misma lista.
    - Ser indexadas y cortadas, lo que permite acceder a elementos específicos de la lista directamente a través de su índice.
    - Ser anidadas, es decir, una lista puede contener otras listas como elementos, lo que permite crear estructuras de datos complejas como matrices.


[!] Operaciones con Listas [!]

También cubriremos las operaciones fundamentales que se pueden realizar con listas, como:

    - Añadir elementos con métodos como ‘append()‘ y ‘extend()‘.
    - Eliminar elementos con métodos como ‘remove()‘ y ‘pop()‘.
    - Ordenar las listas con el método ‘sort()‘ o la función incorporada ‘sorted()‘.
    - Invertir los elementos con el método ‘reverse()‘ o la sintaxis de corte ‘[::-1]‘.
    - Comprender las comprensiones de listas, una forma “pythonica” de crear y manipular listas de manera concisa y eficiente.
"""



"""
[?] - append: Añadir valores
    - len: Muestra la cantidad de valores
"""
puertos_tcp = [21, 22, 25, 80, 443, 8080, 445, 69]
puertos_tcp.append(1337)
print(len(puertos_tcp))
for puerto in puertos_tcp:
	print(f"[+] Este es el puerto {puerto}")

"""
[?] - remove: Borra valores
"""
cve_list = ['CVE-2023-1435', 'CVE-2022-45761', 'CVE-2023-7863']
cve_list.remove('CVE-2022-45761')
print (cve_list)

"""
[?] - sort: Ordena de menor a mayor
"""
puertos_tcp.sort()
print(puertos_tcp)

"""
[?] - reverse: Invierte los valores
"""
attacks = ['Phising', 'DDoS', 'SQL Injection', 'Man In The Middle', 'Cross-Site Scripting']
attacks.reverse()
print(attacks)

"""
[?] Una forma para iterar sobre cada valor
"""
i=0 # Contador
while i < len(attacks):
	print(attacks[i])
	i+=1

"""
[?] Pasar la lista a mayúsculas
"""
attacks_uppercase = [attack.upper()for attack in attacks]
print(attacks_uppercase)

"""
[?] Una forma de juntar dos listas
"""
names = ['Javier', 'Pepe', 'Juan', 'Manuel']
edades = [19, 23, 42, 55]
for name,edad in zip(names,edades):
	print(f"{name} tiene {edad} años")

"""
[?] - clear: Vaciar lista
"""
names.clear()
print(len(names))

"""
[?] - pop: Elimina el último valor
    De esta forma borramos el valor 1 y lo guardamos en una variable
"""
deleted_age=edades.pop(1)
print(edades)
print(f"[!] La edad eliminada ha sido: {deleted_age}")

"""
[?] - insert: Añade valores donde indiquemos
"""
edades.insert(1,23)
print(edades)
