#!/usr/bin/env python3

import re # La librería re permite realizar expresiones regulares para filtrar sobre cadenas de texto

text="Mi gato está en el tejado y mi otro gato está en el jardín"
matches= re.findall("gato",text) # Te muestra las veces que aparece la palabra "gato" en text
print(matches)


text="Hoy estamos a fecha 10/10/2023, mañana estaremos a 11/10/2023"
matches= re.findall("\d{2}\/\d{2}\/\d{4}",text) # Implementamos un patrón en el que indicas que muestre las palabras que contienen (2 digitos / 2 digitos / 4 digitos)
print(matches)


text="Los usuarios pueden contactarnos a soporte@hack4u.io o a info@hack4u.io"
matches= re.findall("(\w+)@(\w+\.\w{2,})",text) # Implementamos dos grupos en el que el primero sean alfanuméricos y en el segundo alfanuméricos más un punto más alfanuméricos
print(matches)                                  # con mínimo 2 dígitos. Para separar estos dos grupos indicamos un delimitador "@"


text="sal,saludar,salir,ejemplosal"
match=re.findall(r"\bsal",text) # Implementamos un patrón en el que indicas que muestre las palabras que empiecen con sal usando la expresión \b
print(match)


text="Mi gato está en el tejado y mi perro está en el jardín"
nuevo_texto=re.sub("gato","perro",text) # Sustituir la palabra "gato" por "perro"
print(nuevo_texto)


text="Campo1,Campo2,Campo3,Campo4,Campo5" # Este texto simula un archivo .csv
nuevo_texto=re.split(",",text) # Crea una tupla dentro de una lista separando cada campo con una , y un espacio
print(nuevo_texto)



"""
Validador de correos
"""

def validar_correo(correo): # Creamos una función llamada validar_correo pidiendo un valor correo

  patron= "[A-Za-z0-9._+-]+@[A-Za-z0-9]+\.[A-Za-z]{2,}" # Creamos el patrón

  if re.findall(patron,correo): # Si la búsqueda es exitosa retorna un True
    return True
  else:
    return False

print(validar_correo("soporte@hack4u.io"))


text="Hoy estamos a fecha 10/10/2023, mañana estaremos a 11/10/2023"
patron=r"\b(\d{2}\/\d{2}\/\d{4})\b"

print(re.findall(patron,text))

for match in re.finditer(patron,text): # Según el patrón creado y el texto itera por cada valor de la lista
  print(f"La fecha es: {match.group(0)}, la cual comienza en la posición {match.start()} y termina en la posición {match.end()}") # Con group mostramos el objeto y
                                                                                                  #con start/end indicamos la posición en la que se encuentra la coincidencia en el texto

