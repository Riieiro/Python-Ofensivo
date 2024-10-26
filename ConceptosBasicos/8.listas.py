#!/usr/bin/env python3

"""
[?] Creamos la lista
"""
my_ports= [21, 441, 445]

"""
[?] Añadimos un valor a la lista existente
"""
my_ports.append(22)
my_ports.append(80)
my_ports.append(443)

"""
[?] Distintas formas de añadir más de un valor a la lista
"""
my_ports.extend([84,85])
my_ports += [88,8080]
my_ports = my_ports + [90,91]

"""
[?] Ordenamos de menor a mayor el contenido de la lista
"""
my_ports = sorted(my_ports)
print()

"""
[?] Borramos el elemento "0" de la lista
"""
del my_ports[0]

"""
[?] Con un bucle iteramos sobre cada elemento de la lista y lo mostramos en pantalla
"""
for port in my_ports:
	print(f"[+] Puerto: {port}")

"""
[?] Mostramos la longitud que tiene la lista
"""
print(f"\n[+] La lista tiene un total de {len(my_ports)} elementos\n")

"""
[?] Creamos la lista
"""
mi_lista = [1, 2, 3, 4, 5, 6, 54, 25, 7, 15, 7, 11]

"""
[?] Imprimimos del elemento 1 hasta el 3
"""
print (mi_lista[1:3])

"""
[?] Imprimimos del elemento 2 hacia adelante
"""
print (mi_lista[2:])

"""
[?] Imprimimos del elemento 2 hacia atrás
"""
print (mi_lista[:2])

"""
[?] Insertamos el valor 6 depués del valor 2 e imprimimos la lista
"""
mi_lista.insert(2,6)
print (mi_lista)

"""
[?] Borramos el último elemento de la lista
"""
mi_lista.pop()
print (mi_lista)

"""
[?] Preguntamos cúal es el índice del valor 7 y lo comprobamos
"""
print (mi_lista.index(7)) #[!] Index solo muestra el primer valor, es decir si el valor 7 está repetido, mostrará el índice del primer 7
print (mi_lista[9])

"""
[?] Creamos una lista en la que el contenido sea un bucle. El bucle consiste en crear dos valores x,y sobre enumerate(mi_lista), la "x" valdría el índice y la "y" el valor.
    De esta forma esta iterando sobre cada elemento de x,y para que cuanto la "y" valga 7, almacene la "x" en la nueva lista
"""
indices = [x for x,y in enumerate(mi_lista) if y==7] 
print(indices)

"""
[?] Comprobamos si los índices son correctos
"""
print(mi_lista[9])
print(mi_lista[11])

"""
[?] Contar cuantas veces aparece el valor 7
"""
print (mi_lista.count(7))

"""
[?] Ordenamos de menor a mayor la lista y la convertimos en un set. Una vez convertida volvemos a cambiar el tipo a lista
    De esta forma conseguimos quitar los valores repetidos de la lista
"""
mi_lista = sorted(mi_lista)
mi_lista = set(mi_lista)
print(mi_lista)
print(type(mi_lista))
mi_lista = list(mi_lista)
print(mi_lista)

"""
[?] Imprimir el máximo, la suma de toda la lista y la media
"""
print(max(mi_lista))

print(sum(mi_lista))

print(sum(mi_lista) / len(mi_lista))
