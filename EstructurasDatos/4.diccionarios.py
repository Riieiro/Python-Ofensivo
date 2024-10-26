#!/usr/bin/env python3	

"""
[!] Características de los Diccionarios [!]

    - Desordenados: Los elementos en un diccionario no están ordenados y no se accede a ellos mediante un índice numérico, sino a través de claves únicas.
    - Dinámicos: Se pueden agregar, modificar y eliminar pares clave-valor.
    - Claves Únicas: Cada clave en un diccionario es única, lo que previene duplicaciones y sobrescrituras accidentales.
    - Valores Accesibles: Los valores no necesitan ser únicos y pueden ser de cualquier tipo de dato.


[!] Operaciones con Diccionarios [!]

Durante la clase, exploraremos cómo realizar operaciones básicas y avanzadas con diccionarios:

    - Agregar y Modificar: Cómo agregar nuevos pares clave-valor y modificar valores existentes.
    - Eliminar: Cómo eliminar pares clave-valor usando del o el método ‘pop()‘.
    - Métodos de Diccionario: Utilizar métodos como ‘keys()‘, ‘values()‘, y ‘items()‘ para acceder a las claves, valores o ambos en forma de pares.
    - Comprensiones de Diccionarios: Una forma elegante y concisa de construir diccionarios basados en secuencias o rangos.


[!] Uso de Diccionarios en Python [!]

    - Almacenamiento de Datos Estructurados: Ideales para almacenar y organizar datos que están relacionados de manera lógica, como una base de datos en memoria.
    - Búsqueda Eficiente: Los diccionarios son altamente optimizados para recuperar valores cuando se conoce la clave, proporcionando tiempos de búsqueda muy rápidos.
    - Flexibilidad: Pueden ser anidados, lo que significa que los valores dentro de un diccionario pueden ser otros diccionarios, listas o cualquier otro tipo de dato.
"""







"""
[?] Filtrar la key por el valor buscado
"""
mi_diccionario = {"nombre": "Javi", "edad": 19, "ciudad": "Madrid"}
print(mi_diccionario["edad"])


"""
[?] Añadir un nuevo valor y key
"""
mi_diccionario["profesion"] = "estudiante"


"""
[?] Borrar un valor
"""
del mi_diccionario["edad"]


"""
[?] Cambiar la key de un valor
"""
mi_diccionario["nombre"] = "Pepe"


"""
[?] Comprobar si existe ese valor
"""
if "ciudad" in mi_diccionario:
	print("[+] Esta clave existe en el diccionario")

"""
[+] Con items podemos iterar sobre el valor y la key
"""
for key,value in mi_diccionario.items():
	print(f"[+] Para la clave {key} tendríamos el valor {value}")


"""
[?] Comprobar la longitud del diccionario
"""
print(len(mi_diccionario))


"""
[?] Vaciar el contenido
"""
mi_diccionario.clear()


"""
[?] Hacer operaciones dentro de un diccionario
"""
cuadrados = {x: x**2 for x in range(6)}
print(cuadrados)


"""
[?] - keys: muestra las keys del diccionario
    - values: muestra los valores del diccionario
"""
print(cuadrados.keys())
print(cuadrados.values())


"""
[?] Juntar dos diccionarios
"""
mi_diccionario = {"nombre": "Javi", "edad": 19, "ciudad": "Madrid"}
mi_diccionario2= {"mascotas": "perro", "profesion": "estudiante"}
mi_diccionario.update(mi_diccionario2)


"""
[?] Comprobar si existe ese valor en el diccionario, si existe te muestra su key, y sino te muestra el mensaje 
"""
print(mi_diccionario.get("nombr", "No encontrado"))


"""
[?] Crear un diccionario dentro de otro
"""
my_dict= {
	"nombre": "Javi",
	"hobbies": {"primero": "música", "segundo": "futbol"},
	"edad": 19
}


"""
[?] Filtrar por el contenido del diccionario anidado
"""
print(my_dict["hobbies"]["segundo"])




