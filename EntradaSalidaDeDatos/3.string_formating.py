cadena= "    Hola    "
print(cadena.strip()) # La función strip() quita los espacios, tabulaciones, saltos de línea...


mayus="HOLA"
print(mayus.lower()) # La función lower() convierte todo el texto en minúscula


minus="hola"
print(minus.upper()) # La función upper() convierte todo el texto en mayúscula


cadena="Hola"
print(cadena.replace('o','x')) # La funcion replace() remplaza los caracteres que queramos por otros


cadena="Hola Mundo"
nueva_cadena = cadena.split() # La función split() crea una lista usando como delimitador los espacios
print(nueva_cadena)


cadena="Hola:Mundo,test"
nueva_cadena=cadena.split(":") # También podemos especificar el delimitador
print(nueva_cadena)


cadena = "Hola mundo"
print(cadena.startswith("H")) # La función startswith devuelve un booleano dependiendo de si la cadena empieza con el valor proporcionado


cadena = "Hola mundo"
print(cadena.endswith("ndo")) # La función endswith devuelve un booleano dependiendo de si la cadena termina con el valor proporcionado


cadena = "Hola mundo"
print(cadena.find("mundo")) # La función find() indica en que posición se encuentra la cadena proporcionada, en caso de que no exista python devolvera un -1


cadena = "Hola mundo"
try:
  print(cadena.index("Python")) # La función index() tiene la misma utilidad que find(), con la diferencia de que podemos controlar el error
except ValueError:
  print("[!] La cadena proporcionada no se encuentra dentro del valor indicado")


cadena= "Esto es una prueba para contar el total de caracteres e que hay en esta frase"
print(f"\n[+] Total de veces que sale el caracter 'e': {cadena.count('e')} ") # La función count() permite contar las veces que sale el caracter proporcionada


cadena = ["Hola", "Mundo"]
print(' '.join(cadena)) # La función join() permite juntar una lista con los espacios o comas que queramos


cadena = "hola mundo"
print(cadena.capitalize()) # La función capitalize() proporciona la cadena con el primer caracter en mayúscula


cadena = "abcd"
print(cadena.isalpha()) # La función isalpha() devuelve un booleano True en el caso de que no contenga números


cadena="123"
print(cadena.isdigit()) # La función isdigit() devuelve un booleano True en el caso de que no contenga caracteres alfabéticos


cadena=" "
print(cadena.isspace()) # La función isspace() devuelve un booleano True en el caso de que el texto sea un espacio


cadena="hola"
print(cadena.islower()) # La función islower() devuelve un booleano True en el caso de que el texto esté en minúsculas


cadena="HOLA"
print(cadena.isupper()) # La función isupper() devuelve un booleano True en el caso de que el texto esté en mayúsculas






