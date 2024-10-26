#!/usr/bin/env python3

import os # Importar la librería os para poder ejecutar comandos en el sistema más adelante
from gestor_notas import GestorNotas # Importar la clase GestorNotas del archivo gestor_notas creado por nosotros



def main(): # Función principal del programa

  gestor=GestorNotas() # Crear objeto gestor de la clase GestorNotas importada del archivo gestor_notas

  while True: # Bucle infinito para ejecutar repetidamente el menú principal

    print(f"\n------------------\nMENU\n-----------------")
    print("1. Agregar una nota")
    print("2. Leer todas las notas")      # Mostrar las opciones posibles
    print("3. Buscar por una nota")
    print("4. Eliminar una nota")
    print("5. Vaciar notas")
    print("6. Salir")
    print("7. Borrar el archivo gestor de notas")

    opcion=input("\n[+] Escoge una opción: ") # Preguntar al usuario una opción y almacenarla en una variable

    if opcion == "1": # Opción 1
      contenido = input("\n[+] Contenido de la nota: ") # Preguntar al usuario el contenido de la nota que queramos agregar y la almacenamos en una variable
      gestor.agregar_nota(contenido) # Llamar a la función agregar_nota creada en la clase GestorNotas, pasándole la variable contenido

    elif opcion == "2": # Opción 2
      notas = gestor.leer_notas() # Metemos en la variable notas la función leer_notas creada en el archivo gestor_notas
      print("\n[+] Mostrando todas las notas:\n")
      for i,nota in enumerate(notas): # Iteramos por cada indice y valor de la lista almacenada en notas
        print(f"{i}: {nota}")

    elif opcion == "3": # Opción 3
      texto_busqueda=input("\n[+] Ingresa el texto a buscar como criterio en las notas: ") # Pedimos al usuario un str y lo almacenamos en una variable
      notas = gestor.buscar_nota(texto_busqueda) # Metemos en la variable notas la función buscar_nota creada en el archivo gestor_notas, pasandole la variable texto_busqueda
      print("\n[+] Mostrando las notas que coinciden con el criterio de la búsqueda: \n")

      for i,nota in enumerate(notas): # Itera por cada índice y valor de la lista notas
        print(f"{i+1}: {nota}")

    elif opcion == "4": # Opción 4
      index=int(input("\n[+] Introduce el índice de la nota que quieres borrar: ")) # Pedimos al usuario un int y lo almacenamos en una variable
      gestor.eliminar_nota(index) # Llamamos a la función eliminar_nota del archivo gestor_notas y le pasamos la variable index

    elif opcion == "5": # Opción 5
      gestor.vaciar_notas() # Llamamos a la función vaciar_notas del archivo gestor_notas
      print("\n[+] Se han vaciado todas las notas")

    elif opcion=="6": # Opción 6
      break # Parar el bucle infinito para salir del menú principal

    elif opcion=="7": # Opción 7
      os.system('del notas.pkl' if os.name=='nt' else 'rm notas.pkl') # Ejecutamos un comando a nivel de sistema dependiendo si el os es Linux o Windows

    else: # Opción incorrecta
      print("\n[!] La opción indicada es incorrecta\n")

    input(f"\n[+] Presiona <Enter> para continuar...") # Input para que al presiónar <Enter> continue el programa

    os.system('cls' if os.name == 'nt' else 'clear') # Usando la librería os, ejecutamos un comando en el sistema. Empleamos un condicional para poder identificar si el os
                                                     # es Linux o Windows



if __name__ == '__main__':
  main()


