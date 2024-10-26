#!usr/bin/env python3

first_number = 6
second_number = 8

"""
[?] Suma
"""
print(first_number + second_number)

"""
[?] Resta
"""
print(first_number - second_number)

"""
[?] Multiplicación
"""
print(first_number * second_number)

"""
[?] División
"""
print(first_number / second_number)

"""
[?] 6 elevado a 8
"""
print(first_number ** second_number)

"""
[?] Con format indicamos que separe los números por comas, y con replace remplazamos las comas por puntos
"""
print("{:,}".format(first_number ** second_number).replace(",","."))

"""
[?] Resto
"""
print(first_number % second_number)

"""
[?] Creamos variables con contenido string
"""
first_str = "Hola"
second_str = " "
third_str = "mundo" 

"""
[?] Imprime el elemento 2 3 veces
"""
print(first_str[2]*3)

"""
[?] Creamos dos listas y las unimos
"""
odd_element = [1, 3, 5, 7, 9]
even_element = [2, 4, 6, 8, 10]
result = list( zip(odd_element, even_element))

print(result)
