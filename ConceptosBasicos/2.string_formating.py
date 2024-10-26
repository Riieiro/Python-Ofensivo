#!/usr/bin/env python3

name = "Pepe"
rol = "Estudiante"
edad=29

"""
Operador % (Porcentaje)

También conocido como “interpolación de cadenas“, este método clásico utiliza marcadores de posición como ‘%s‘ para cadenas, ‘%d‘ para enteros, o ‘%f‘ 
para números de punto flotante.
"""
print("[+] Hola, mi nombre es %s y soy un %s, tengo %d años" % (name, rol, edad))

"""
Método format()

Introducido en Python 2.6, permite una mayor flexibilidad y claridad. Utiliza llaves ‘{}‘ como marcadores de posición dentro de la cadena y puede incluir detalles sobre el formato de la salida.
"""
print("[+] Hola, soy {0} y tengo {1} años. No es broma mi nombre es {0}".format(name, edad))

"""
F-Strings (Literal String Interpolation)

F-Strings ofrece una forma concisa y legible de incrustar expresiones dentro de literales de cadena usando la letra ‘f‘ antes de las comillas de apertura y llaves para indicar dónde se insertarán las variables o expresiones.
"""
print(f"[+] Hola, soy {name} y tengo {edad} años. No es broma mi nombre es {name}")
